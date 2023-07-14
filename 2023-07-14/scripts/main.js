const favorite_movie = 'служебный роман'
let dict_ru = {
    alert_success: 'BINGO!!!',
    alert_unsuccess: 'А вот и нет',
    guess_question: 'Какой мой любимый фильм?\nЧтобы останосить игру введите stop\nЧтобы перейти к следующему заданию введите next task',
    stop: 'stop',
    next_task: 'next task',
    next_task_info: 'А теперь переходим ко второй задаче'
}

// Task 1
function guess_the_film(guess) {
    if (guess.toLowerCase() == favorite_movie) {
        alert(dict_ru.alert_success)
    } else {
        alert(dict_ru.alert_unsuccess)
    }
}

while (true) {
    let answer = prompt(dict_ru.guess_question)
        if (answer.toLowerCase() == dict_ru.stop) {
        throw ''
    }
    else if (answer.toLowerCase() == dict_ru.next_task) {
        break
    }
    guess_the_film(answer)
}
alert(dict_ru.next_task_info)

// Task 2
let myArray = ['a', 'b', 'c']
myArray[0] = 'слово'
myArray[1] = 'Это предложение'
myArray[2] = 'б'

// А теперь часть с двумя звездочками, итерируемся :)
for (let i = 0; i < myArray.length; i++) {
    alert(myArray[i])
}
