def remove_duplicates(lt):
    result = []
    for i in lt:
        if i not in result:
            result.append(i)
    return result

def main():
    l=[1,2,3,4,1,2]
    print(remove_duplicates(l))
    
main()