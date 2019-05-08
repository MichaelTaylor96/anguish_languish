function qs(selector) {
    return document.querySelector(selector)
}

function qsa(selector) {
    return document.querySelectorAll(selector)
}

let input = ''
result = []

qs('button').addEventListener('click', function() {
    input = qs('input').value
    words = input.split(' ')
    for (let word of words) {
        fetch(`https://api.datamuse.com/words?sl=${word}`).then(response => response.json())
            .then(json => {
                for (let word of json) {
                    if word['word']
                }
                result.push([json[5]['word']+' ', words.indexOf(word)])
                result.sort(function(a, b) {
                    return a[1] - b[1]
                })
                console.log(result)
            })
    }   
})