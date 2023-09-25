# Sudoku Solver and Generator

This application is designed to create a Flask server that can generate valid Sudoku boards and solve any valid Sudoku puzzles, providing solved solutions as responses.

DEMO API: **http://sudoku-env.eba-jtqfjqia.us-east-1.elasticbeanstalk.com/**

## Board Generation

To implement the Sudoku board generator, we've introduced a `Board` class. Within this class:

- The `full_board` function generates a random Sudoku solution board with all numbers filled in.
- The `make_puzzle` function randomly removes numbers from the Sudoku solution to create a puzzle. This process ensures that each puzzle always has a solution. However, please note that this approach guarantees at least one solution but not necessarily a unique one.

## Solving Sudoku Puzzles

To address the uniqueness issue associated with the `Board` class, we've developed a secondary class called `SudokuSolver`. This class:

- Accepts the puzzle as an argument during instantiation.
- Utilizes its `start_solver` function to find all possible solutions while verifying the uniqueness of the puzzle's solution.
- Achieves this by employing the backtracking algorithm, keeping track of the count of solutions found, and storing the first solution encountered.

## Sudoku API

- /api/makeboard: This endpoint, accessible via GET requests, invokes the 'sudoku_board_handler' function and returns a freshly generated Sudoku puzzle.

- /api/fullgame: Accepting GET requests, this endpoint triggers 'sudoku_full_game_handler' and returns both a Sudoku puzzle and its corresponding solution.

- /api/solver: Designed for POST requests with a Sudoku puzzle input, this endpoint invokes 'sudoku_solvable_handler' and returns a solution if the puzzle is valid. Before processing, the solver API ensures the puzzle's correct formatting using the 'check_if_full_board' function. If the puzzle lacks a unique solution or has formatting issues, it gracefully responds with a 400 status code.

Feel free to explore this repository to see how Sudoku puzzles can be generated and solved using Flask!

## How to start on Local Machine

### Prerequisites


### Clone the Repository

Open your terminal or command prompt and run the following command to clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-flask-app.git
```

### Setting up a Virtual Environment

It's a good practice to create a virtual environment for your Flask app to manage dependencies. Navigate to the project directory and run the following commands:

```bash
cd your-flask-app
python -m venv venv
```

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate

```

- On macOS and Linux:

```bash
source venv/bin/activate
```

### Install Dependencies
While inside the virtual environment, install the required Python packages:
```bash
pip install -r requirements.txt
```
### Running the Flask App
Now that you have set up the environment and installed dependencies, you can run the Flask app. In the project directory, run the following command:

```bash
python application.py
```

Your Flask app should now be running locally. You should see output indicating that the app is running, typically on **http://127.0.0.1:5000/**.

Open a web browser and navigate to the provided address to access your Flask app.

### Stopping the Flask App
To stop the Flask app, simply press **Ctrl+C** in the terminal where the app is running. This will shut down the development server.