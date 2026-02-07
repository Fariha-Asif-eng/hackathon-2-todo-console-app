from setuptools import setup, find_packages

setup(
    name="todo-cli-app",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo=src.cli.cli_app:main',
        ],
    },
    install_requires=[],
    author="AI Assistant",
    description="A command-line todo application",
    python_requires='>=3.13',
)