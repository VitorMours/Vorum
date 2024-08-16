let buttons = document.getElementsByClassName("flash-message-delete-button")


for(let message of buttons){
          message.addEventListener("click", () => {
                    list_element = message.parentElement;
                    list_element.remove()
          });
}