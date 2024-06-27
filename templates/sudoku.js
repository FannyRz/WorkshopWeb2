let selectedCell = null;

document.addEventListener("DOMContentLoaded", function() {
    generateSudoku();
});

// Fonction pour générer un nouveau Sudoku
function generateSudoku() {
    const sudokuTable = document.getElementById('sudokuTable');
    sudokuTable.innerHTML = '';

    // Crée une grille de Sudoku vide 9x9
    const grid = generateCompleteSudoku();

    // Enlève des chiffres pour créer le puzzle
    const puzzleGrid = removeNumbers(grid);

    // Remplit la table avec le puzzle
    for (let i = 0; i < 9; i++) {
        const row = document.createElement('tr');
        for (let j = 0; j < 9; j++) {
            const cell = document.createElement('td');
            const input = document.createElement('input');
            input.setAttribute('type', 'number');
            input.setAttribute('min', '1');
            input.setAttribute('max', '9');
            input.addEventListener('click', () => selectCell(input));
            if (puzzleGrid[i][j] !== 0) {
                input.value = puzzleGrid[i][j];
                input.setAttribute('disabled', 'true');
            }
            cell.appendChild(input);
            row.appendChild(cell);
        }
        sudokuTable.appendChild(row);
    }
}

// Sélectionne une cellule
function selectCell(input) {
    if (input.disabled) return;

    if (selectedCell) {
        selectedCell.style.backgroundColor = '';
    }
    selectedCell = input;
    selectedCell.style.backgroundColor = 'lightblue';
}

// Remplit la cellule sélectionnée avec le chiffre donné
function fillSelectedCell(number) {
    if (selectedCell && !selectedCell.disabled) {
        selectedCell.value = number;
    }
}

// Génère une grille de Sudoku complète
function generateCompleteSudoku() {
    const grid = Array.from({ length: 9 }, () => Array(9).fill(0));
    fillSudoku(grid);
    return grid;
}

// Remplit la grille de Sudoku de manière valide
function fillSudoku(grid) {
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (grid[i][j] === 0) {
                shuffleArray(numbers);
                for (let num of numbers) {
                    if (isValidPlacement(grid, i, j, num)) {
                        grid[i][j] = num;
                        if (fillSudoku(grid)) {
                            return true;
                        }
                        grid[i][j] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}

// Vérifie si le placement est valide
function isValidPlacement(grid, row, col, num) {
    for (let x = 0; x < 9; x++) {
        if (grid[row][x] === num || grid[x][col] === num) {
            return false;
        }
    }
    const startRow = Math.floor(row / 3) * 3;
    const startCol = Math.floor(col / 3) * 3;
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (grid[startRow + i][startCol + j] === num) {
                return false;
            }
        }
    }
    return true;
}

// Mélange un tableau
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Enlève des chiffres pour créer le puzzle
function removeNumbers(grid) {
    const puzzleGrid = grid.map(row => row.slice());
    let attempts = 5;

    while (attempts > 0) {
        let row = Math.floor(Math.random() * 9);
        let col = Math.floor(Math.random() * 9);
        while (puzzleGrid[row][col] === 0) {
            row = Math.floor(Math.random() * 9);
            col = Math.floor(Math.random() * 9);
        }
        const backup = puzzleGrid[row][col];
        puzzleGrid[row][col] = 0;

        const copyGrid = puzzleGrid.map(row => row.slice());
        if (!hasUniqueSolution(copyGrid)) {
            puzzleGrid[row][col] = backup;
            attempts--;
        }
    }
    return puzzleGrid;
}

// Vérifie si la grille a une solution unique
function hasUniqueSolution(grid) {
    return solveSudoku(grid, true);
}

// Résout la grille de Sudoku
function solveSudoku(grid, checkUnique) {
    const findEmpty = (grid) => {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (grid[i][j] === 0) {
                    return [i, j];
                }
            }
        }
        return null;
    };

    const solve = (grid) => {
        const emptySpot = findEmpty(grid);
        if (!emptySpot) {
            return true;
        }
        const [row, col] = emptySpot;
        for (let num = 1; num <= 9; num++) {
            if (isValidPlacement(grid, row, col, num)) {
                grid[row][col] = num;
                if (solve(grid)) {
                    return true;
                }
                grid[row][col] = 0;
            }
        }
        return false;
    };

    if (!checkUnique) {
        return solve(grid);
    } else {
        const originalGrid = grid.map(row => row.slice());
        solve(grid);
        const solvedGrid = grid.map(row => row.slice());

        // Try solving again and ensure we get the same solution
        grid = originalGrid.map(row => row.slice());
        let solutions = 0;

        const countSolutions = (grid) => {
            const emptySpot = findEmpty(grid);
            if (!emptySpot) {
                solutions++;
                return solutions > 1;
            }
            const [row, col] = emptySpot;
            for (let num = 1; num <= 9; num++) {
                if (isValidPlacement(grid, row, col, num)) {
                    grid[row][col] = num;
                    if (countSolutions(grid)) {
                        return true;
                    }
                    grid[row][col] = 0;
                }
            }
            return false;
        };

        countSolutions(grid);
        return solutions === 1;
    }
}

// Vérifie si la solution est correcte
function checkSolution() {
    const sudokuTable = document.getElementById('sudokuTable');
    const inputs = sudokuTable.getElementsByTagName('input');
    const grid = Array.from({ length: 9 }, () => Array(9).fill(0));

    let index = 0;
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const value = parseInt(inputs[index].value);
            if (!isNaN(value)) {
                grid[i][j] = value;
            }
            index++;
        }
    }

    for (let i = 0; i < 9; i++) {
        const row = grid[i];
        const column = grid.map(row => row[i]);
        if (!isValidArray(row) || !isValidArray(column)) {
            alert('La solution est incorrecte !');
            return;
        }
    }

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const block = [];
            for (let k = 0; k < 3; k++) {
                for (let l = 0; l < 3; l++) {
                    block.push(grid[i * 3 + k][j * 3 + l]);
                }
            }
            if (!isValidArray(block)) {
                alert('La solution est incorrecte !');
                return;
            }
        }
    }

    alert('La solution est correcte !');
}

// Vérifie si un tableau contient tous les chiffres de 1 à 9 sans répétition
function isValidArray(array) {
    const sortedArray = array.slice().sort((a, b) => a - b);
    for (let i = 0; i < 9; i++) {
        if (sortedArray[i] !== i + 1) {
            return false;
        }
    }
    return true;
}
