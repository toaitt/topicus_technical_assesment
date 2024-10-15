import time


class TestCase:
    def __init__(self, test_suit, test_condition, name, pre_condition=None):
        self.test_suit = test_suit
        self.test_condition = test_condition
        self.name = name
        self.step_list = []
        self.pre_conditions = pre_condition if pre_condition else []
        self.results = {}
        self.success_list = []

    def execute_test_case(self, step_list, mapping_table=None):
        all_passed = True
        print('----------------------------')
        print(f"Execute {self.name}")
        print('----------------------------')
        for pre_condition in self.pre_conditions:
            pre_step = None
            for case in mapping_table:
                if case['Case'] == pre_condition:
                    pre_step = case['Step']
                    break
            pre_condition.execute_test_case(step_list=pre_step, mapping_table=mapping_table)
        for i, step in enumerate(step_list):
            self.step_list.append(step)
            # Execute the step and store the result
            try:
                result = step.execute_step()

            except Exception as e:
                result = [e, False]
            print(f"Step {i}: {'Pass' if result[1] else 'Failed'}")
            self.results[i] = result
            self.success_list.append(result[1])
            if not result[1]:
                print(result[0])
                all_passed = False
        if all_passed:
            print("Test case executed successfully")
        else:
            print("Test case executed Failed")
        return all_passed


class Step:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def execute_step(self):
        time.sleep(0.1)
        return self.func(*self.args, **self.kwargs)