package tools;

import java.util.Arrays;

/** Small dense matrix helper used for contribution testing. */
public class Matrix {

    private final int rows;
    private final int cols;
    private final double[][] values;

    public Matrix(int rows, int cols) {
        if (rows <= 0 || cols <= 0) {
            throw new IllegalArgumentException("dimensions must be positive");
        }
        this.rows = rows;
        this.cols = cols;
        this.values = new double[rows][cols];
    }

    public static Matrix of(double[][] source) {
        Matrix matrix = new Matrix(source.length, source[0].length);
        for (int i = 0; i < source.length; i++) {
            if (source[i].length != matrix.cols) {
                throw new IllegalArgumentException("rows must have equal length");
            }
            System.arraycopy(source[i], 0, matrix.values[i], 0, matrix.cols);
        }
        return matrix;
    }

    public static Matrix identity(int size) {
        Matrix matrix = new Matrix(size, size);
        for (int i = 0; i < size; i++) {
            matrix.values[i][i] = 1.0;
        }
        return matrix;
    }

    public int rows() {
        return rows;
    }

    public int cols() {
        return cols;
    }

    public double get(int row, int col) {
        return values[row][col];
    }

    public void set(int row, int col, double value) {
        values[row][col] = value;
    }

    public Matrix plus(Matrix other) {
        if (rows != other.rows || cols != other.cols) {
            throw new IllegalArgumentException("shapes must match");
        }
        Matrix result = new Matrix(rows, cols);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result.values[i][j] = values[i][j] + other.values[i][j];
            }
        }
        return result;
    }

    /** Returns the matrix product of this and other. */
    public Matrix times(Matrix other) {
        if (cols != other.rows) {
            throw new IllegalArgumentException("inner dimensions must match");
        }
        Matrix result = new Matrix(rows, other.cols);
        for (int i = 0; i < rows; i++) {
            for (int k = 0; k < cols; k++) {
                double left = values[i][k];
                for (int j = 0; j < other.cols; j++) {
                    result.values[i][j] += left * other.values[k][j];
                }
            }
        }
        return result;
    }

    public Matrix transpose() {
        Matrix result = new Matrix(cols, rows);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result.values[j][i] = values[i][j];
            }
        }
        return result;
    }

    @Override
    public String toString() {
        return Arrays.deepToString(values);
    }
}
