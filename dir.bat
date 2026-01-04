@echo off
echo Initializing APT Learn platform structure...

REM Root folders
mkdir mentor-backend
mkdir ide-frontend
mkdir shared
mkdir scripts

REM Mentor backend structure
mkdir mentor-backend\src
mkdir mentor-backend\src\mentor
mkdir mentor-backend\src\ide
mkdir mentor-backend\src\utils
mkdir mentor-backend\mentor
mkdir mentor-backend\workspace

REM Shared contracts
mkdir shared\contracts

REM Create empty files
type nul > mentor-backend\src\server.js
type nul > mentor-backend\src\mentor\lesson-engine.js
type nul > mentor-backend\src\mentor\lesson-loader.js
type nul > mentor-backend\src\mentor\mentor-router.js
type nul > mentor-backend\src\ide\file-api.js
type nul > mentor-backend\src\ide\execute-api.js
type nul > mentor-backend\src\utils\fs-utils.js

type nul > mentor-backend\mentor\lessons.json
type nul > mentor-backend\package.json
type nul > mentor-backend\.env

type nul > ide-frontend\README.md
type nul > shared\contracts\mentor-step.schema.json
type nul > README.md

echo.
echo APT Learn base structure created successfully.
pause
