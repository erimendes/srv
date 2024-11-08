-- Script MariaDB 

-- Exclui o banco de dados se ele existir 
DROP DATABASE IF EXISTS social_media; 

-- Cria o banco de dados 
CREATE DATABASE social_media; 

-- Usa o banco de dados
 USE social_media; 

-- Tabela 'UserData' 
DROP  TABLE IF EXISTS UserData; 

CREATE  TABLE UserData ( 
    id CHAR ( 36 ) NOT  NULL  PRIMARY KEY, 
    data VARCHAR ( 160 ) NOT  NULL
 );