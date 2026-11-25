import json
import os
import xml.etree.ElementTree as ET


def extract_xml_data(file_path):
    print(f"Startar extrahering från: {file_path}")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Filen {file_path} hittades inte!")

    tree = ET.parse(file_path)
    root = tree.getroot()
    
    extracted_records = []
    
    for order in root.findall('order'):
        record = {
            "order_id": order.get('id'),
            "customer": order.find('customer').text,
            "amount": float(order.find('amount').text),
            "currency": order.find('amount').get('currency'),
            "status": order.find('status').text
        }
        extracted_records.append(record)
        
    return extracted_records

if __name__ == "__main__":
    xml_file = "data/sample.xml"
    data = extract_xml_data(xml_file)
    
    print("Extraherad data (JSON-format):")
    print(json.dumps(data, indent=2, ensure_ascii=False))