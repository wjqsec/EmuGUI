def generate_dev_config(dev_name):
    return []

def generate_dev_header(dev_name):
    return f'''
                dev = qdev_new(\"{dev_name}\");
                qdev_realize_and_unref(dev, pcms->pcibus, &error_fatal);
                '''