```mermaid
graph TD
    A[Generate Synthetic Dataset] --> B[Create Feature Names]
    B --> C[Convert to Pandas DataFrame]
    C --> D[Add Noise Features]
    D --> E[Generate Dataset Variations]
    E --> F[Low Sparsity, Low Redundancy]
    E --> G[Low Sparsity, High Redundancy]
    E --> H[High Sparsity, Low Redundancy]
    E --> I[High Sparsity, High Redundancy]
    E --> J[Baseline Dataset]

    F --> K[Dataset 1]
    G --> L[Dataset 2]
    H --> M[Dataset 3]
    I --> N[Dataset 4]
    J --> O[Baseline Dataset]

    D --> P[Add Noise (1000 features)]
    P --> Q[Final Noisy Dataset]
