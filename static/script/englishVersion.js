const englishElements = document.querySelectorAll(".en")
const frenchElements = document.querySelectorAll(".fr")
const toggleEnglish = document.querySelectorAll(".toggleEnglish")

toggleEnglish.forEach(e => {
    e.checked = false;
    e.addEventListener("change", toggle)
})

function toggle(event) {
    toggleEnglish.forEach(e => {
        e.checked = event.target.checked;
    })

    for (const frenchElement of frenchElements) {
        frenchElement.classList.toggle("hidden")
    }
    for (const englishElement of englishElements) {
        englishElement.classList.toggle("hidden")
    }
}

