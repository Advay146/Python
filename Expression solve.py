class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            print(f"📘 Expression: {self.expression}")
            print(f"✅ Result: {result}")
        except Exception as e:
            print("❌ Error in expression:", e)

# Example usage
expr1 = ExpressionSolver("5 + 3 * 2")
expr1.solve()

expr2 = ExpressionSolver("(10 - 2) / 4")
expr2.solve()

expr3 = ExpressionSolver("15 ** 2")
expr3.solve()