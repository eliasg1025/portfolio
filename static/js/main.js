const skillsCard = document.getElementById('skills-and-tools');
const experienceCard = document.getElementById('experience');

let heightCard = (
    skillsCard.clientHeight >= experienceCard.clientHeight
        ? experienceCard.clientHeight
        : skillsCard.clientHeight
);

if (heightCard < 500) {
    heightCard = 500;
}

skillsCard.style.height = `${heightCard}px`;
experienceCard.style.height = `${heightCard}px`;
