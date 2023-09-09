import copy

import sudoku


def sudoku_board_genarator():
    board = sudoku.Board()

    while True:
        ps = sudoku_board_solver(board.puzzle)
        if ps[0]:
            break
        else:
            board.change_board()
            board.change_puzzle()
    return board


def sudoku_board_solver(p):
    ps = sudoku.SudokuSolver(p)
    if ps.start_solver() == 1:
        return [True, ps]
    else:
        return [False]


def input_check(game):
    if isinstance(game, list):
        if all(isinstance(a, list) for a in game) and all(
            ele in list(range(0, 10)) for list_ in game for ele in list_
        ):
            if len(game) == 9 and all(len(row) == 9 for row in game):
                return True
    return False


def sodoku_full_game_handler():
    board = sudoku_board_genarator()
    ans = board.boardf
    p = board.puzzle

    return {"status_code": 201, "message": {"ans": ans, "puzzle": p, "user_attempt": p}}


def sodoku_board_handler():
    board = sudoku_board_genarator()

    return {"status_code": 201, "message": board.puzzle}


def sodoku_solvable_handler(game):
    if input_check(game):
        ps = sudoku_board_solver(game)
        if ps[0]:
            return {"status_code": 201, "message": ps[1].ans}

        return {"status_code": 401, "message": "Invalid Board"}

    return {"status_code": 401, "message": "Invalid input"}


if __name__ == "__main__":
    test1 = sudoku_board_genarator()
    print(test1.boardf)
    # print(test1.puzzle)
    test2 = copy.deepcopy(test1.puzzle)
    test2[5][6] = 30
    # print(input_check(test1.boardf))

    # print(input_check(test2))
    # test2[5][6]="4"
    # print(input_check(test2))
    # print( sodoku_full_game_handler())
    # print( sodoku_board_handler())
    print(sodoku_solvable_handler(test1.puzzle))
    print(sodoku_solvable_handler(test2))
    print(test2 == test1.puzzle)
