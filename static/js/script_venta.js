//FORMA DEL CODIGO DE LA PROFE CECILIA
    document.addEventListener('DOMContentLoaded', function() {
    const addButton = document.getElementById('add-form');
    const formsetContainer = document.getElementById('formset-container');
    const totalForms = document.getElementById('id_items_venta-TOTAL_FORMS');

    // Función para actualizar los índices de los formularios
    function updateFormIndexes() {
        const forms = formsetContainer.getElementsByClassName('item-form');
        for (let i = 0; i < forms.length; i++) {
            const form = forms[i];

            // Actualizar todos los elementos 'input', 'select' y 'label' del formulario con el nuevo índice
            form.querySelectorAll('input, select, label').forEach(element => {
                if (element.id) {
                    element.id = element.id.replace(/-(\d+)-/, `-${i}-`);
                }
                if (element.name) {
                    element.name = element.name.replace(/-(\d+)-/, `-${i}-`);
                }
                if (element.htmlFor) { // Para los labels
                    element.htmlFor = element.htmlFor.replace(/-(\d+)-/, `-${i}-`);
                }
            });
        }
        // Actualizamos el total de formularios en el formset
        totalForms.value = forms.length;
    }

    // Agregar nuevo formulario
    addButton.addEventListener('click', function(e) {
        e.preventDefault();
        const newForm = formsetContainer.children[0].cloneNode(true); // Clonar el primer formulario como base

        // Limpiar los valores del formulario clonado
        newForm.querySelectorAll('input').forEach(input => {
        if (input.type === 'text' || input.type === 'number') {
            input.value = ''; // Limpiar los campos de texto y numéricos
        }
        });
        newForm.querySelectorAll('select').forEach(select => select.selectedIndex = 0);

        formsetContainer.appendChild(newForm); // Añadir el nuevo formulario al contenedor
        updateFormIndexes(); // Actualizar los índices de todos los formularios
    });

    // Eliminar formulario
    formsetContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-form')) {
            e.preventDefault();
            const form = e.target.closest('.item-form');
            form.remove();
            updateFormIndexes();
        }
    });
});
