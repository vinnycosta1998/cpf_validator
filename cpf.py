class CPF():

    def __init__(self, cpf):
        self.cpf = cpf

        self.list_cpf = []
        self.product_first_nine_digits = []
        self.product_first_ten_digits = []

        self.first_digit_verificator = None
        self.second_digit_verificator = None
        
        self.validate_cpf()
        self.validate_first_digit_verificator()

    def validate_cpf(self):
        self.cpf = self.cpf.replace(".", "").replace("-", "")
        print("CPF sem caractheres", self.cpf)
        self.list_cpf = list(self.cpf)
        print("TAMANHO CPF", len(self.cpf))
        if len(self.list_cpf) != 11:
            raise ValueError("O CPF deve ter 11 digítos")
        try:
            for i in range(0, 11):
                self.list_cpf[i] = int(self.list_cpf[i])
            print("CPF na lista", self.list_cpf)
        except ValueError:
            raise ValueError("CPF com caractheres inválido")

    def validate_first_digit_verificator(self):
        index = 0
        self.first_nine_digits_on_cpf = self.list_cpf[0:9]
        for i in range(10, 1, -1):
            self.product_first_nine_digits.append(self.first_nine_digits_on_cpf[index] * i)
            index += 1
        sum_of_nine_first_digits = sum(self.product_first_nine_digits)
        split_for_eleven = sum_of_nine_first_digits % 11
        if split_for_eleven < 2:
            self.first_digit_verificator = 0
        else:
            self.first_digit_verificator = 11 - split_for_eleven
        self.validate_second_digit_verificator()

    def validate_second_digit_verificator(self):
        index = 0
        self.first_ten_digits_on_cpf = self.list_cpf[0:10]
        for j in range(11, 1, -1):
            self.product_first_ten_digits.append(self.first_ten_digits_on_cpf[index] * j)
            index += 1
        sum_of_ten_first_digits = sum(self.product_first_ten_digits)
        split_for_eleven = sum_of_ten_first_digits % 11
        if split_for_eleven < 2:
            self.second_digit_verificator = 0
        else:
            self.second_digit_verificator = 11 - split_for_eleven
        self.verify_cpf()

    def verify_cpf(self):
        self.last_two_digits_on_cpf = self.list_cpf[9:11]
        return ( self.last_two_digits_on_cpf[0] == self.first_digit_verificator and self.last_two_digits_on_cpf[1] == self.second_digit_verificator)
        
if __name__ == "__main__":
    CPF()
