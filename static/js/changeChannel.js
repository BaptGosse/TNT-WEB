const actionButtons = document.querySelectorAll(".channel")
actionButtons.forEach((actionButton)=>{
    actionButton.addEventListener('click', () => {
        fetch(`/action/${actionButton.id}`, {method: ['POST']});
    });
});