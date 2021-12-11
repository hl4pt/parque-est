CREATE TABLE `entradas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `matricula` varchar(45) DEFAULT NULL,
  `hr_entrada` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `lugarlivres` (
  `lugar` int NOT NULL AUTO_INCREMENT,
  `livre` int NOT NULL,
  `matricula` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`lugar`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `registos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `matricula` text NOT NULL,
  `tempo_total` int DEFAULT NULL,
  `custo` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8;

CREATE TABLE `saidas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hr_saida` datetime DEFAULT NULL,
  `matricula` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;
DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `desocupar_lugar`(
IN s_matricula varchar(45))
BEGIN
    UPDATE lugarlivres SET livre = 0, matricula = NULL
    WHERE matricula = s_matricula;
end$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `hora_entrada`(
        IN s_matricula VARCHAR(45)
)
BEGIN
    SELECT hr_entrada FROM entradas WHERE matricula = s_matricula ORDER BY id DESC LIMIT 1;
end$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `lugares_livres`()
BEGIN
    SELECT lugar FROM lugarlivres WHERE livre = 0;
end$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `ocupar_lugar`(
        IN s_matricula VARCHAR(45),
        IN s_lugar INT
)
BEGIN
    UPDATE lugarlivres SET livre = 1, matricula = s_matricula WHERE lugar = s_lugar;
end$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `registo`(
        IN s_matricula VARCHAR(45),
        IN s_tempo_total INT,
        IN s_custo FLOAT
)
BEGIN
    INSERT INTO registos (matricula, tempo_total, custo)
    VALUES (s_matricula, s_tempo_total, s_custo);
end$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `registo_entrada`(
        IN s_matricula VARCHAR(45),
        IN s_entrada DATETIME
)
BEGIN
    INSERT INTO entradas (matricula, hr_entrada)
    VALUES (s_matricula, s_entrada);
end$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `registo_saida`(
        IN s_matricula VARCHAR(45),
        IN s_saida DATETIME
)
BEGIN
    INSERT INTO saidas (matricula, hr_saida)
    VALUES (s_matricula, s_saida);
end$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `tb_entradas`()
BEGIN
select * from entradas;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `tb_lugareslivres`()
BEGIN
select * from lugarlivres;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `tb_registos`()
BEGIN
select * from registos;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `tb_saidas`()
BEGIN
select * from saidas;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`admin`@`%` PROCEDURE `verificar_saida`(
        IN s_matricula VARCHAR(45)
)
BEGIN
   SELECT IF(matricula IS NULL, 0, 1)
    FROM lugarlivres WHERE matricula = s_matricula;
end$$
DELIMITER ;
