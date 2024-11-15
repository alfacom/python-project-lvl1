### Hexlet tests and linter status:
[![Actions Status](https://github.com/alfacom/python-project-lvl1/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alfacom/python-project-lvl1/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d6db9ceb52afb5dd82c0/maintainability)](https://codeclimate.com/github/alfacom/python-project-lvl1/maintainability)

# Brain Games
Набор простеньких игр для тренировки логики.

## Установка

Требуется python v3.12
Скачивайте whl-файл со страницы [последнего релиза](https://github.com/alfacom/python-project-lvl1/releases/latest) и запустите команду:
```bash
python3.12 -m pip install --user *.whl
```
Если появится ошибка 
```
WARNING: The scripts brain-calc, brain-even, brain-games, brain-gcd, brain-prime and brain-progression are installed in '/root/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```
То не забудьте добавить в PATH директорию `/root/.local/bin`:
```bash
PATH=$PATH:/root/.local/bin
```


## Demo's
Демки отрисованы с учетом, что репозиторий был скачан полностью.
При установке по инструкции выше дописывать make для запуска игр не нужно.

### Demo Brain Calc and Brain Even
В игре Brain Calc необходимо найти результат вычисления.

В игре Brain Even необходимо указать, четное число или нет.

![asciicinema](gif/calc_even.gif)

### Demo Brain GCD

В игре Brain GCD необходимо найти НОД(Наибольший Общий Делитель)
![asciicinema](gif/gcd.gif)

### Demo Brain Progression

В игре Brain Progression необходимо найти пропущенный элемент прогрессии
![asciicinema](gif/progr.gif)

### Demo Brain Prime

В игре Brain Prime необходимо указать, простое число или нет.
![asciicinema](gif/prime.gif)