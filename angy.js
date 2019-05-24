function qs(selector) {
    return document.querySelector(selector)
}

function qsa(selector) {
    return document.querySelectorAll(selector)
}

let input = ''
let result = []

qs('button').addEventListener('click', function() {
    result = []
    input = qs('input').value
    words = input.split(' ')
    for (let word of words) {
        fetch(`https://api.datamuse.com/words?sl=${word}&md=f`).then(response => response.json())
            .then(json => {
                json.shift()
                console.log(json)
                
                let rankedWords = json.sort(function(a, b) {
                    let aFreq = parseFloat(a["tags"][0].split(":")[1])
                    let bFreq = parseFloat(b["tags"][0].split(":")[1])
                    aRank = aFreq + (a["score"])
                    bRank = bFreq + (b["score"])
                    return bRank - aRank
                })
                console.log(rankedWords)
                result.push([rankedWords[0]["word"]+' ', words.indexOf(word)])
                result.sort(function(a, b) {
                    return a[1] - b[1]
                })
                console.log(result)
            })
    }   
})