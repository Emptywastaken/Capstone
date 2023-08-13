document.addEventListener('DOMContentLoaded', ()=>{

    // edit function
    document.querySelectorAll('.btn-outline-secondary').forEach((edit_btn) => {
        
        edit_btn.onclick = () => {
            
            const parentDiv = edit_btn.parentElement.parentElement.parentElement;
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

        const parentDiv = delete_btn.parentElement.parentElement.parentElement;
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
    
    // translation function
    document.querySelectorAll('.btn-outline-primary').forEach((translate_btn => {
        translate_btn.onclick = () => {

            const parentDiv = translate_btn.parentElement.parentElement.parentElement;
            const text = parentDiv.querySelector('.wordTranslation').querySelector('strong');
            const translation = text.getAttribute('data-translation');
            console.log(translation);
            const translationTag = text.querySelector('span');
            translationTag.innerHTML = '';
            translationTag.innerHTML = ' / ' + translation;

        }
    }))
})

const flags = {
    'af': 'AF',
    'sq': 'AL',
    'am': 'AM',
    'ar': 'AR',
    'hy': 'AM',
    'az': 'AZ',
    'eu': 'ES',
    'be': 'BY',
    'bn': 'BD',
    'bs': 'BA',
    'bg': 'BG',
    'ca': 'ES',
    'ceb': 'PH',
    'ny': 'MW',
    'zh-CN': 'CN',
    'zh-TW': 'TW',
    'co': 'FR',
    'hr': 'HR',
    'cs': 'CZ',
    'da': 'DK',
    'nl': 'NL',
    'en': 'GB',
    'eo': 'EO',
    'et': 'EE',
    'tl': 'PH',
    'fi': 'FI',
    'fr': 'FR',
    'fy': 'NL',
    'gl': 'ES',
    'ka': 'GE',
    'de': 'DE',
    'el': 'GR',
    'gu': 'IN',
    'ht': 'HT',
    'ha': 'NG',
    'haw': 'US',
    'iw': 'IL',
    'hi': 'IN',
    'hmn': 'HMN',
    'hu': 'HU',
    'is': 'IS',
    'ig': 'NG',
    'id': 'ID',
    'ga': 'IE',
    'it': 'IT',
    'ja': 'JP',
    'jw': 'ID',
    'kn': 'IN',
    'kk': 'KZ',
    'km': 'KH',
    'rw': 'RW',
    'ko': 'KR',
    'ku': 'KU',
    'ky': 'KG',
    'lo': 'LA',
    'la': 'VA',
    'lv': 'LV',
    'lt': 'LT',
    'lb': 'LU',
    'mk': 'MK',
    'mg': 'MG',
    'ms': 'MY',
    'ml': 'MY',
    'mt': 'MT',
    'mi': 'NZ',
    'mr': 'IN',
    'mn': 'MN',
    'my': 'MM',
    'ne': 'NP',
    'no': 'NO',
    'or': 'IN',
    'ps': 'AF',
    'fa': 'IR',
    'pl': 'PL',
    'pt': 'PT',
    'pa': 'IN',
    'ro': 'RO',
    'ru': 'RU',
    'sm': 'WS',
    'gd': 'GB',
    'sr': 'RS',
    'st': 'LS',
    'sn': 'ZW',
    'sd': 'PK',
    'si': 'LK',
    'sk': 'SK',
    'sl': 'SI',
    'so': 'SO',
    'es': 'ES',
    'su': 'ID',
    'sw': 'TZ',
    'sv': 'SE',
    'tg': 'TJ',
    'ta': 'IN',
    'tt': 'RU',
    'te': 'IN',
    'th': 'TH',
    'tr': 'TR',
    'tk': 'TM',
    'uk': 'UA',
    'ur': 'PK',
    'ug': 'CN',
    'uz': 'UZ',
    'vi': 'VN',
    'cy': 'GB',
    'xh': 'ZA',
    'yi': 'IL',
    'yo': 'NG',
    'zu': 'ZA',
    'he': 'IL',
    'zh': 'CN'
};