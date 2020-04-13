const sumEvenNumbers = input => input.reduce((total, number) => (number % 2 === 0 ? total + number : total), 0)
