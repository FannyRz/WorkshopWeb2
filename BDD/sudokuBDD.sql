-- MySQL Script generated by MySQL Workbench
-- Tue Jun 25 16:52:23 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sudokuDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sudokuDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sudokuDB` DEFAULT CHARACTER SET utf8 ;
USE `sudokuDB` ;

-- -----------------------------------------------------
-- Table `sudokuDB`.`JOUEUR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sudokuDB`.`JOUEUR` (
  `id_joueur` INT NOT NULL,
  `pseudo` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `prenom` VARCHAR(45) NOT NULL,
  `date_creation` DATE NOT NULL,
  `nationalite` VARCHAR(45) NOT NULL,
  `date_naissance` DATE NULL,
  `score` INT NOT NULL DEFAULT 0,
  `mot_de_passe` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_joueur`),
  UNIQUE INDEX `id_joueur_UNIQUE` (`id_joueur` ASC) VISIBLE,
  UNIQUE INDEX `pseudo_UNIQUE` (`pseudo` ASC) VISIBLE,
  UNIQUE INDEX `mot_de_passe_UNIQUE` (`mot_de_passe` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sudokuDB`.`JOUR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sudokuDB`.`JOUR` (
  `id_jour` INT NOT NULL,
  `date` DATE NOT NULL,
  `id_joueur` INT NOT NULL,
  PRIMARY KEY (`id_jour`),
  UNIQUE INDEX `id_jour_UNIQUE` (`id_jour` ASC) VISIBLE,
  INDEX `id_joueur_idx` (`id_joueur` ASC) VISIBLE,
  CONSTRAINT `id_joueur`
    FOREIGN KEY (`id_joueur`)
    REFERENCES `sudokuDB`.`JOUEUR` (`id_joueur`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sudokuDB`.`SUDOKU`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sudokuDB`.`SUDOKU` (
  `id_sudoku` INT NOT NULL,
  `difficulte` INT NOT NULL,
  `case_init` LONGTEXT NOT NULL,
  PRIMARY KEY (`id_sudoku`),
  UNIQUE INDEX `id_sudoku_UNIQUE` (`id_sudoku` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sudokuDB`.`SESSION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sudokuDB`.`SESSION` (
  `id_session` INT NOT NULL,
  `nbr_erreur` INT NULL,
  `temps` DATETIME NOT NULL,
  `id_jour` INT NOT NULL,
  `id_sudoku` INT NOT NULL,
  PRIMARY KEY (`id_session`),
  INDEX `id_jour_idx` (`id_jour` ASC) VISIBLE,
  INDEX `id_sudoku_idx` (`id_sudoku` ASC) VISIBLE,
  CONSTRAINT `id_jour`
    FOREIGN KEY (`id_jour`)
    REFERENCES `sudokuDB`.`JOUR` (`id_jour`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_sudoku`
    FOREIGN KEY (`id_sudoku`)
    REFERENCES `sudokuDB`.`SUDOKU` (`id_sudoku`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;