from metaflow import FlowSpec, step

class MoreComplexFlow(FlowSpec):

    @step
    def start(self):
        self.numbers = [1, 2, 3, 4, 5]
        print(f"Starting with numbers: {self.numbers}")
        self.next(self.square, foreach='numbers')

    @step
    def square(self):
        self.squared = self.input ** 2
        print(f"Number {self.input} squared is {self.squared}")
        self.next(self.join_squares)

    @step
    def join_squares(self, inputs):
        self.squares = [step.squared for step in inputs]
        print(f"All squared numbers: {self.squares}")
        self.next(self.sum_squares)

    @step
    def sum_squares(self):
        self.total = sum(self.squares)
        print(f"Sum of squares: {self.total}")

        # Determine branch key as a self attribute
        self.branch = 'large' if self.total > 50 else 'small'
        self.next({'large': self.large, 'small': self.small}, condition='branch')

    @step
    def large(self):
        print(f"The total {self.total} is large!")
        self.next(self.end)

    @step
    def small(self):
        print(f"The total {self.total} is small!")
        self.next(self.end)

    @step
    def end(self):
        print("Flow finished!")

if __name__ == '__main__':
    MoreComplexFlow()
