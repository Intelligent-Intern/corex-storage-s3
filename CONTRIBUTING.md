# Contributing to CoreX Storage - S3

Thank you for your interest in contributing to CoreX Storage - S3! We welcome contributions from the community and appreciate your efforts in improving this project. This document outlines our guidelines and best practices for contributing.

## Table of Contents

- [Reporting Issues](#reporting-issues)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Contribution](#your-first-contribution)
- [Pull Request Process](#pull-request-process)
- [Coding Guidelines](#coding-guidelines)
- [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [License](#license)
- [Questions](#questions)

## Reporting Issues

If you encounter any bugs or have suggestions for improvements, please first search our [GitHub Issues](https://github.com/intelligent-intern/corex/issues) to see if the issue has already been reported. If not, please create a new issue including:

- **Description:** A clear and concise description of the issue.
- **Steps to Reproduce:** Detailed steps to reproduce the problem.
- **Expected vs. Actual Behavior:** What you expected to happen versus what occurred.
- **Environment Details:** OS, Python version, and any other relevant details.
- **Additional Context:** Any other information that may help resolve the issue.

## Suggesting Enhancements

We welcome ideas for new features or improvements. When suggesting enhancements, please provide:

- **Feature Description:** A detailed explanation of the proposed feature.
- **Use Case:** How the feature would benefit users.
- **Implementation Ideas:** (Optional) Your thoughts on how to implement the feature.
- **Potential Impact:** Any possible trade-offs or impacts on existing functionality.

## Your First Contribution

If you're new to contributing, here’s a simple workflow to get started:

1. **Fork the Repository:** Click the "Fork" button at the top right of the repository.
2. **Clone Your Fork:**
   ~~~bash
   git clone https://github.com/your-username/corex-storage-s3.git
   ~~~
3. **Create a New Branch:**
   ~~~bash
   git checkout -b feature/your-feature-name
   ~~~
4. **Make Your Changes:** Implement your changes, ensuring you follow our coding guidelines.
5. **Write Tests:** Add tests to cover your changes.
6. **Commit Your Changes:** Write clear, descriptive commit messages.
   ~~~bash
   git commit -m "Add: [brief description of feature/bug fix]"
   ~~~
7. **Push Your Changes:**
   ~~~bash
   git push origin feature/your-feature-name
   ~~~
8. **Open a Pull Request:** Submit a pull request against the `main` branch of the original repository.

## Pull Request Process

When opening a pull request, please ensure:

- **Clear Title and Description:** Summarize your changes and link any related issues (e.g., "Fixes #123").
- **Explanation:** Describe why the changes are necessary and include any relevant screenshots or test results.
- **Passing Tests:** Make sure your changes pass all tests and adhere to the project’s style guidelines.
- **Documentation Updates:** Update relevant documentation if your changes affect how the project is used.

## Coding Guidelines

- **Python Version:** This project supports Python 3.6 and above.
- **Project Structure:** Follow the existing file structure and naming conventions.
- **Testing:** Include unit tests for any new functionality or bug fixes.
- **Documentation:** Ensure functions and classes have proper docstrings and update the README when necessary.

## Style Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style.
- Use linters such as `flake8` or formatters like `black` to maintain consistency.
- Write clear and concise code with inline comments where needed.

## Commit Message Guidelines

- Use the present tense (e.g., "Add feature" instead of "Added feature").
- Keep the subject line concise (ideally under 50 characters).
- Provide additional details in the commit message body if necessary.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## Questions

If you have any questions or need further assistance, please open an issue or contact us at js@intelligent-intern.com.

Thank you for contributing to CoreX Storage - S3!
