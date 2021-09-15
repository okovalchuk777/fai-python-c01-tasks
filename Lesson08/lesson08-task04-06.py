class MyOwnNotaNumberError(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self):
        self.init_info = 'да'
        self.init_info01 = 'да'
        self.init_info_list01 = []
        self.init_info_list02 = []
        self.init_info_list03 = []
        self.equip_tuple = {}

    def __str__(self):
        pass

    def equipment_reception(self):
        while self.init_info == 'да':
            self.init_info01 = 'да'
            self.init_info = input("Введите название оборудования: ")
            self.init_info_list01.append(self.init_info)
            while self.init_info01.isdigit() is False:
                try:
                    self.init_info01 = str(input("Введите количество оборудования: "))
                    if self.init_info01.isdigit():
                        self.init_info_list02.append(self.init_info01)
                        self.init_info01 = '1'
                    else:
                        self.init_info01 = 'да'
                        raise MyOwnNotaNumberError("Введённое значение не является числом. Введите число.")
                except MyOwnNotaNumberError as err:
                    print(err)
            self.init_info = input("Введите название подразделения: ")
            self.init_info_list03.append(self.init_info)
            self.equip_tuple = {'оборудование': self.init_info_list01, 'количество': self.init_info_list02,
                                'подразделение': self.init_info_list03}
            self.init_info = input(
                "Информация сохранена. Вы готовы внести информацию о следующем товаре? Ввведите да или нет: ")
        print(f'Заказ принят на {self.equip_tuple}.')


class OfficeEquipment:
    def __init__(self, manufacturer, model, quantity):
        self.manufacturer = manufacturer
        self.model = model
        self.quantity = quantity

    def __str__(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, quantity, printer_dpi, print_speed, printer_paper_format):
        super().__init__(manufacturer, model, quantity)
        self.printer_dpi = printer_dpi
        self.print_speed = print_speed
        self.printer_paper_format = printer_paper_format
        self.printer_dict_shortly = {'manufacturer': self.manufacturer, 'model': self.model, 'quantity': self.quantity}

    def __str__(self):
        pass


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, quantity, scanner_type_of_sensor_installed, scanner_optical_depth,
                 scanning_speed):
        super().__init__(manufacturer, model, quantity)
        self.scanner_type_of_sensor_installed = scanner_type_of_sensor_installed
        self.scanner_optical_depth = scanner_optical_depth
        self.scanning_speed = scanning_speed
        self.scanner_dict_shortly = {'manufacturer': self.manufacturer, 'model': self.model, 'quantity': self.quantity}

    def __str__(self):
        pass


class MultifunctionalPrinter(OfficeEquipment):
    def __init__(self, manufacturer, model, quantity, mfp_dpi, mfp_print_speed, mfp_paper_format):
        super().__init__(manufacturer, model, quantity)
        self.mfp_dpi = mfp_dpi
        self.mfp_print_speed = mfp_print_speed
        self.mfp_paper_format = mfp_paper_format
        self.mfp_dict_shortly = {'manufacturer': self.manufacturer, 'model': self.model, 'quantity': self.quantity}

    def __str__(self):
        pass


printer01 = Printer('HP', 'LaserJet Pro M15w', 135, '600x600', 18, 'A4')
scanner01 = Scanner('HP', 'ScanJet Pro 2000 s2', 85, 'Laser', '24bit', 'A4')
mfp01 = MultifunctionalPrinter('Xerox', 'ALTALINK B8055', 15, '600x600', 35, 'A4')
print(printer01.printer_dict_shortly)
print(scanner01.scanner_dict_shortly)
print(mfp01.mfp_dict_shortly)
order = Warehouse()
order.equipment_reception()
