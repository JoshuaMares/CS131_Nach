from functools import reduce

def remove_invalid_emails(inputs):
  return list(filter(lambda email : True if ("@" in email and "." in email[email.index("@"):]) else False , inputs))

print(remove_invalid_emails(["matt@matthewwang.me", "notreal", "stay@home", "st.ay@home"]))

def count_edu_emails(inputs):
  valid_emails = remove_invalid_emails(inputs)
  return reduce(lambda accum, current: accum+1 if ("edu" in current[current.index("@"):]) else accum, valid_emails, 0)

print(count_edu_emails(["matt@matthewwang.me", "tree@stanford.edu", "beaver@mit.edu", "thisisntreallyan@edu.email"]))

def generate_email_validator(predicate):
    return lambda inputs : list(filter(predicate, inputs))

bad_validator = generate_email_validator(lambda x: len(x) > 3)
print(bad_validator(["a", "thisissonotanemail", "matt@matthewwang.me"]))

def compare_validators(strings_list, predicates_list):
    #filter -> reduce -> reduce
    return list(map(lambda list: len(list), map(lambda validator: validator(strings_list), map(lambda pred: generate_email_validator(pred), predicates_list))))

print(compare_validators(["matt@matthewwang.me", "makarlATucd.edu", "a@a.a"], [lambda x: len(x) > 3, lambda x: x != "makarlATucd.edu"]))

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n

def fizzbuzz_list(start, end):
    return [fizzbuzz(n) for n in range(start, end+1)]

print(fizzbuzz_list(10,15))
