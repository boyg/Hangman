#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "engine.h"

#define FILENAME "web.txt"
#define P_FACTOR 0.85
#define BUFSIZE  256

int getDim(FILE* dataFile);
double** parseData(FILE* dataFile, int dim);
void calcPageRank(double** connectivityMat, int dim);

int main(void) {
	FILE* dataFile;
	int dim;
	double** connectivityMat = NULL;

	int error = fopen_s(&dataFile, FILENAME, "r"); // fopen_s returns 0 if file successfully opens

	if (error) {
		fprintf(stderr, "Unable to open file: %s\n", FILENAME);
		system("pause");
		return 1;
	}

	if (dataFile != NULL) {
		dim = getDim(dataFile);
		connectivityMat = parseData(dataFile, dim);
		calcPageRank(connectivityMat, dim);
	}

	free(connectivityMat);

	system("pause");
	return 0;
}

/* getDim
 * takes a pointer to a data file as an input
 * and returns the dimension of the connectivity matrix contained inside */
int getDim(FILE* dataFile) {
	int tempSize;         // local variable for size
	char buffer[BUFSIZE]; // string containing first line of file

	/* get length of string containing first line of file */
	tempSize = (int) strlen(fgets(buffer, BUFSIZE, dataFile));

	/* 'reset' the file's internal pointer to the beginning of the file */
	fseek(dataFile, 0, SEEK_SET);

	/* check if text file was created in Windows and contains '\r'
	If true reduce strlen by 2 in order to omit '\r' and '\n' from each line
	Else    reduce strlen by 1 in order to omit '\n' from each line */
	if (strchr(buffer, '\r') != NULL)
		tempSize -= 2;
	else
		tempSize -= 1;

	/* account for spaces in between columns */
	return (tempSize + 1) / 2;
}

/* parseData
 * takes a pointer to a data file and the dimension of the matrix as an input
 * and returns a double pointer to the connectivity matrix inside */
double** parseData(FILE* dataFile, int dim) {
	int row, col;
	double** connectivityMat = NULL;

	char buffer[BUFSIZE];

	/* dynamically allocate a 2D array of appropriate size */
	connectivityMat = (double**)calloc(dim, sizeof(double*));            // allocate array of pointers ("columns")
	for (row = 0; row < dim; row++)                                      // iterate along the row
		connectivityMat[row] = (double*)calloc(dim, sizeof(double)); // create columns of size dim

	/* copy the file into the 2D array */
	row = 0;
	while (fgets(buffer, BUFSIZE, dataFile)) { // read from the file line by line

		for (col = 0; col < dim; col++) {
			buffer[col] = buffer[2 * col]; // get rid of spaces in between numbers

			if (buffer[col] == '1')
				connectivityMat[row][col] = 1.0;
			else
				connectivityMat[row][col] = 0.0;
		}
		row++;
	}
	return connectivityMat;
}

/* calcPageRank
 * takes in a double pointer to the connectivity matrix and its dimension as an input
 * and prints the resultant vector to standard output */
void calcPageRank(double** connectivityMat, int dim) {
	Engine* ep = engOpen(NULL);
	mxArray* ConnectivityMatrix = mxCreateDoubleMatrix(dim, dim, mxREAL);
	mxArray* result = NULL;
	int i, j;
	double* flatMat = malloc((dim * dim) * sizeof(double));

	/* Flatten 2D array into 1D array with column-major order */
	for (j = 0; j < dim; j++)
		for (i = 0; i < dim; i++)
			flatMat[(j*dim)+i] = connectivityMat[i][j];

	/* Place array into MATLAB */
	memcpy((void*)mxGetPr(ConnectivityMatrix), (void*)flatMat, (dim * dim) * sizeof(double));
	engPutVariable(ep, "ConnectivityMatrix", ConnectivityMatrix);

	/* Run PageRank script */
	engEvalString(ep, "[rows, columns] = size(ConnectivityMatrix)");
	engEvalString(ep, "dimension = size(ConnectivityMatrix, 1)");
	engEvalString(ep, "columnsums = sum(ConnectivityMatrix, 1)");
	engEvalString(ep, "p = 0.85"); // hard-coded P_FACTOR
	engEvalString(ep, "zerocolumns = find(columnsums~=0)");
	engEvalString(ep, "D = sparse( zerocolumns, zerocolumns, 1./columnsums(zerocolumns), dimension, dimension)");
	engEvalString(ep, "StochasticMatrix = ConnectivityMatrix * D");
	engEvalString(ep, "[row, column] = find(columnsums==0)");
	engEvalString(ep, "StochasticMatrix(:, column) = 1./dimension");
	engEvalString(ep, "Q = ones(dimension, dimension)");
	engEvalString(ep, "TransitionMatrix = p * StochasticMatrix + (1 - p) * (Q/dimension)");
	engEvalString(ep, "PageRank = ones(dimension, 1)");
	engEvalString(ep, "for i = 1:100 PageRank = TransitionMatrix * PageRank; end");
	engEvalString(ep, "PageRank = PageRank / sum(PageRank)");

	/* Print result */
	result = engGetVariable(ep, "PageRank");
	printf("NODE  RANK\n");
	printf("---   ----\n");
	for (i = 0; i < dim; i++)
		printf("%d     %.4f\n", i + 1, *(mxGetPr(result) + i));

	/* Manage memory */
	mxDestroyArray(ConnectivityMatrix);
	mxDestroyArray(result);
	result = NULL;
	free(flatMat);
	engClose(ep);

	return;
}
