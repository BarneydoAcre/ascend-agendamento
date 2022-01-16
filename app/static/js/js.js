var cell = document.querySelectorAll('#id_telefone');
var cellLabel = document.querySelectorAll('#label_id_telefone');

for (let i=0;i<cell.length;i++) {
    cell[i].addEventListener('blur', function() {
        while (cell[i].value.includes('-') || cell[i].value.includes('(') || cell[i].value.includes(')') || cell[i].value.includes(' ')) {
            cell[i].value = cell[i].value.replace('-','')
            cell[i].value = cell[i].value.replace('(','')
            cell[i].value = cell[i].value.replace(')','')
            cell[i].value = cell[i].value.replace(' ','')
        }
        if (cell[i].value.length == 10 || cell[i].value.length == 11) {
            var cell1 = cell[i].value.slice(0,2);
            var cell2 = cell[i].value.slice(2,7);
            var cell3 = cell[i].value.slice(7,11);
            var cellResult = '('+cell1+') '+cell2+'-'+cell3;
            cell[i].value = cellResult;

            cellLabel[i].innerHTML = 'Número de telefone válido!';
            cell[i].style = 'border-bottom: 1px solid green;';
            cellLabel[i].style = 'color: green;';
            
            return true;
        }if (cell[i].value.length == 14 || cell[i].value.length == 15){
            cellLabel[i].innerHTML = 'Número de telefone válido!';
            cell[i].style = 'border-bottom: 1px solid green;';
            cellLabel[i].style = 'color: green;';
            
            return true;
        }if (cell[i].value.length == 0) {
            cellLabel[i].innerHTML = 'Telefone'; 
            cell[i].style = '';
            cellLabel[i].style = '';
            
            return true;
        }else{
            cellLabel[i].innerHTML = 'Número de telefone inválido!';
            cell[i].style = 'border-bottom: 1px solid red;';
            cellLabel[i].style = 'color: red;';

            return false;
        }
    })
} 