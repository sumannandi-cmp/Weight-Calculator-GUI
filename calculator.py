from sympy import symbols, Eq, solve


class WeightCalculator:
    @staticmethod
    def calculate(n1, atomic_masses, ratios, weights, total, selected_index):
        n = int(n1)
        variables = symbols(f'x:{n + 1}')
        equations = []

        for i in range(n - 1):
            a = float(atomic_masses[i].get()) * float(ratios[i].get())
            b = float(atomic_masses[i + 1].get()) * float(ratios[i + 1].get())
            coeffs = [0] * (n + 1)
            coeffs[i] = 1 / a
            coeffs[i + 1] = -1 / b
            equations.append(Eq(sum(c * v for c, v in zip(coeffs, variables)), 0))

        coefficients = [1] * n + [-1]
        equations.append(Eq(sum(c * v for c, v in zip(coefficients, variables)), 0))

        coeffs = [0] * (n + 1)
        if selected_index == 0:
            coeffs[-1] = 1
            constant = float(total)
        else:
            coeffs[selected_index - 1] = 1
            constant = float(weights[selected_index - 1].get())

        equations.append(Eq(sum(c * v for c, v in zip(coeffs, variables)) - constant, 0))

        solution = solve(equations, variables)

        return {
            'weights': [solution[variables[i]] for i in range(n)],
            'total': solution[variables[-1]]
        }
