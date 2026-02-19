def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            length = len(lines)
            total = 0

            # print(f"length: {length}")

            for line in lines:
                parts = line.strip().split(',')
                # print(f"parts: {parts}")
                try:
                    salary = float(parts[1])
                    total += salary
                except ValueError:
                    continue
            
            avarage = total / length if length > 0 else total

            # print(f"total: {total}, avarage: {avarage}")
            return (total, avarage)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0)
    
# Example usage
total, avarage = total_salary("task1/sal.txt")
print(f"result: total: {total}, avarage: {total, avarage}")
