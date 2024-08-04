from flask import Flask, request, render_template
from models.vehicles import vehicles

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    fit_results = {}
    initial_dims = {}
    error_message = ""
    form_data = {
        'pallet_length': '',
        'pallet_width': '',
        'pallet_height': '',
        'num_pallets': '',
        'total_weight': '',
        'stackable': 'yes'
    }

    if request.method == 'POST':
        try:
            # Retrieve and store form values
            form_data['pallet_length'] = request.form.get('pallet_length', '')
            form_data['pallet_width'] = request.form.get('pallet_width', '')
            form_data['pallet_height'] = request.form.get('pallet_height', '')
            form_data['num_pallets'] = request.form.get('num_pallets', '')
            form_data['total_weight'] = request.form.get('total_weight', '')
            form_data['stackable'] = request.form.get('stackable', 'yes')

            # Convert values to correct types
            pallet_length = float(form_data['pallet_length']) if form_data['pallet_length'] else 0
            pallet_width = float(form_data['pallet_width']) if form_data['pallet_width'] else 0
            pallet_height = float(form_data['pallet_height']) if form_data['pallet_height'] else 0
            num_pallets = int(form_data['num_pallets']) if form_data['num_pallets'] else 1
            total_weight = float(form_data['total_weight']) if form_data['total_weight'] else 0

            pallet_size = (pallet_length, pallet_width, pallet_height)

            # Store initial dimensions
            initial_dims = {
                'Length': pallet_length,
                'Width': pallet_width,
                'Height': pallet_height,
                'Number of Pallets': num_pallets,
                'Total Weight': total_weight
            }

            # Calculate fit results
            for vehicle_name, vehicle in vehicles.items():
                try:
                    fit, total_length, total_width, total_height, total_pallet_weight = vehicle.check_fit(
                        pallet_size,
                        total_weight / num_pallets,  # Distribute total weight over pallets
                        total_weight,
                        num_pallets,
                        form_data['stackable'] == 'yes'
                    )
                    fit_results[vehicle_name] = {
                        'fits': 'Yes' if fit else 'No',
                        'Total Length': total_length,
                        'Total Width': total_width,
                        'Total Height': total_height,
                        'Total Weight': total_pallet_weight
                    }
                except ValueError as e:
                    error_message = f"Error in vehicle {vehicle_name}: {str(e)}"
                    break

        except ValueError:
            error_message = "Please enter valid numbers for the fields."

    return render_template('index.html', fit_results=fit_results, initial_dims=initial_dims, error=error_message, form_data=form_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)