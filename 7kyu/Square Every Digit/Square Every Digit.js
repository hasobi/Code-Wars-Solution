const squareDigits = num => {
    // rubah integer menjadi string dengan men-split.
    const digits = num.toString().split('')

    // JS bisa menkuadratkan string jadi langsung saja dikuadratkan
    const squaredDigits = digits.map(n => n * n)

    // hasil masih beruba string yang tidak menjadi satu sehingga
    // harus digabung agar sesuai instruksi soal
    const result = squaredDigits.join('')

    return +result
}