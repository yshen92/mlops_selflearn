# MLOps Zoomcamp: Self-Learning Journey

This repository documents a self-learning journey through various concepts of MLOps, based on the MLOps Zoomcamp by DataTalks.Club. It includes materials, code examples, and homework from the course.

## Modules

This repository is organized into modules, each covering a specific area of MLOps:

1.  **[01-intro](./01-intro/)**: Introduction to MLOps.
    *   Covers basic concepts, course setup, and initial data exploration for model building.
2.  **[02-experiment-tracking](./02-experiment-tracking/)**: Experiment Tracking and Model Management
    *   Focuses on using MLflow for tracking experiments, managing models, and utilizing the model registry.
3.  **[03-orchestration](./03-orchestration/)**: Orchestration and ML Pipelines
    *   Explores using Prefect for creating, deploying, and observing ML workflows.
4.  **[04-deployment](./04-deployment/)**: Model Deployment
    *   Covers various deployment strategies including web services (Flask, Docker, MLflow), streaming (Kinesis, Lambda), and batch scoring (Prefect).
5.  **[05-monitoring](./05-monitoring/)**: Model Monitoring
    *   Details setting up monitoring environments, calculating metrics with Evidently, visualizing with Grafana, and debugging models.
6.  **[06-best-practices](./06-best-practices/)**: Best Practices
    *   Discusses testing (pytest, Docker Compose, LocalStack), code quality (linting, formatting, pre-commit hooks, Makefiles), Infrastructure-as-Code (Terraform), and CI/CD (GitHub Actions).

## General Structure of Each Module

Each module typically contains:
*   Jupyter notebooks or Python scripts with code examples.
*   Links to relevant course videos and slides.
*   Data used for the exercises.
*   Homework assignments.
*   A `README.md` file with detailed information about the module's content and specific setup instructions if any (e.g., `requirements.txt`).
*   A "Notes" section for community contributions and additional resources.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/DataTalksClub/mlops-zoomcamp.git # Or your fork
    cd mlops-zoomcamp
    ```
2.  **Explore the Modules:**
    *   You can navigate through the modules sequentially (recommended for a structured learning path) or jump to specific topics of interest.
    *   Each module's `README.md` provides an overview and links to learning materials.
    *   Check for `requirements.txt` or other setup instructions within each module if you plan to run the code.

## Contributing

This repository is primarily a personal learning log, but contributions that enhance learning for others are welcome!
*   **Add Notes:** If you have useful notes, summaries, or links related to a module, feel free to add them to the "Notes" section of the respective module's `README.md`.
*   **Fix Errors:** If you find any errors in the code or documentation, please open an issue or submit a pull request.
*   **Suggest Improvements:** Suggestions for better explanations or additional relevant topics are appreciated.

When contributing notes, please try to follow the existing format if possible.

## License

This project is primarily for educational purposes. While no specific license is currently applied to the root of this repository, content within specific modules or linked resources may be subject to their own licensing terms. If you plan to reuse or distribute any part of this repository, please ensure you comply with any applicable licenses.

It is recommended to add a general open-source license (e.g., MIT License) if broader sharing and contribution are intended. You can do this by creating a `LICENSE` file in the root directory.
For example, an MIT License would look like this:

```
MIT License

Copyright (c) [Year] [Your Name/Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
