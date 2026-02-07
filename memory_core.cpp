include <cmath>
include <vector>

extern "C" {
    double cosine_similarity(double* a, double* b, int size) {
        double dot = 0.0, mag_a = 0.0, mag_b = 0.0;
        for (int i = 0; i < size; ++i) {
            dot += a[i] * b[i];
            mag_a += a[i] * a[i];
            mag_b += b[i] * b[i];
        }
        if (mag_a == 0 || mag_b == 0) return 0.0;
        return dot / (sqrt(mag_a) * sqrt(mag_b));
    }

    int find_best_match(double* query, double* db, int rows, int cols) {
        int best_idx = -1;
        double max_sim = -1.0;
        
        for (int i = 0; i < rows; ++i) {
            double sim = cosine_similarity(query, &db[i * cols], cols);
            if (sim > max_sim) {
                max_sim = sim;
                best_idx = i;
            }
        }
        return best_idx;
    }
}
