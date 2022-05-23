window.addEventListener('load', () => {
    const params = (new URL(document.location)). searchParams;
    const LOC = params.get('location');
    const comEd = params.get('comEd');

    document.getElementById('result-LOC').innerHTML = LOC;
    document.getElementById('result-comed').innerHTML = comEd;
})