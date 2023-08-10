document.addEventListener('DOMContentLoaded', ()=>{

    // edit function
    document.querySelectorAll('.btn-outline-secondary').forEach((edit_btn) => {
        
        edit_btn.onclick = () => {
            
            const parentDiv = edit_btn.parentElement.parentElement;
            const text = parentDiv.querySelector('.wordTranslation').querySelector('strong');
            const form = parentDiv.querySelector('.wordTranslation').querySelector('span');
            const wordId = parentDiv.getAttribute('data-id');
            const buttonElement = edit_btn.parentElement;

            
            text.style.display = 'block';

            // making edit button disappear
            edit_btn.style.display = 'none';
            console.log(edit_btn);
            text.style.display = 'none';
            
            const inputField =document.createElement('input');
            inputField.value = text.innerHTML;
            inputField.required = true;
            inputField.setAttribute('type', 'text');
            inputField.setAttribute('maxlength', '250');
            inputField.style.height = 'auto';
            inputField.className = 'form-control';
            inputField.style.marginTop = '4px';
            
            //creating save btn
            const save_btn = document.createElement('button');
        
            // setting style attrs
            save_btn.className = "btn btn-primary btn-sm";
            save_btn.innerHTML = "Save";
        
            // ajax request to edit post
            save_btn.onclick = () => {
               fetch(`/edit/${wordId}`, {
                method: 'PUT',
                body: JSON.stringify({
                    translation: inputField.value
                })
               })
               .then(() => {
                    // console.log(result);
        
                    inputField.style.display = "none";
                    save_btn.style.display = "none";
                    text.innerHTML = inputField.value;
                    text.style.display = "inline";
                    edit_btn.style.display = "inline";
               });
           }
            buttonElement.prepend(save_btn);
            form.append(inputField);
            
            console.log(text);
            console.log(form);
        }
    })

    // delete function 
    document.querySelectorAll('.btn-outline-danger').forEach((delete_btn) => {

        const parentDiv = delete_btn.parentElement.parentElement;
        const wordId = parentDiv.getAttribute('data-id');
        
        // ajax request to edit post
        delete_btn.onclick = () => {
           fetch(`/edit/${wordId}`, {
            method: 'DELETE',
           })
           .then(() => {
                // console.log(result);
                parentDiv.style.display = 'none';

           });
       }
        
    })
    
})