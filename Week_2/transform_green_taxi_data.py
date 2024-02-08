if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    # Specify your transformation logic here
    print(f"Preprocessing: rows with zero passengers and zero trip distance: {data['passenger_count'].isin([0] & data['trip_distance'].isin([0])).sum()}")

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    def to_snake_case(name):
        if name.endswith('ID'):
            name = name[:-2] + '_ID'  # Add underscore before 'ID'
        return name.lower()  # Convert the entire string to lowercase

    data.columns = [to_snake_case(column) for column in data.columns]
    
    data.columns = (data.columns
                    .str.replace(' ','_')
    )

    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() ==0, 'There are rides with zero passengers'

    assert output['trip_distance'].isin([0]).sum() ==0, 'There are rides with zero trip distance'

    assert 'vendor_id' in output.columns, 'Column vendor_id does not exist in the DataFrame'
