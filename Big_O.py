# # # -----  O(n) --------

# # def print_items(n):
# #     for i in range(n):
# #         print(i)
        

# # print_items(10)
# # # Time complexity  = O(n)



# # # ------ Drop Constants - Drop constants, just observe trend as n increases ------

# # def print_items(n):
# #     for i in range(n):
# #         print(i)
        
# #     for j in range(n):
# #         print(j)

# # print_items(10)
# # # Time complexity  = O(n + n) = O(2n) => O(n)




# # #  ----- O(n^2) --------

# # def print_items(n):
# #     for i in range(n):
# #         for j in range(n):
# #             print(i, j)
# #         print("Done")
            
    
# # print_items(10)
# # # Time complexity  = O(n * n) = O(2n) => O(n^2) 


# #  ----- Drop Non-dominants--------

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)
        
#     for k in range(n):
#         print(k)
            
    
# print_items(10)
# # Time complexity  = O(n^2) + O(n) =  O(n^2 + n) NB: n will be insignificant when n becomes larger
# # n^2 is dominant and n becomes non-dominant so we drop the n





# ---- O(n) --------
# def print_item(n):
#     for i in range(n):
#         print(i)
        
        
# print_item(100)


# ---- Drop constant----- O(2n)  === O(n)

# def print_item(n):
#     for i in range(n):
#         print(i)
        
#     for j in range(n):
#         print(j)
        
        
# print_item(10)


# # ----- O(n^2) ------

# def print_item(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)
            
            
# print_item(10)

# ----- Drop Non-Dominant------ O(n^2 + n) == O(n^2)

# def print_item(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)
            
#     for k in range(n):
#         print(k)
            
# print_item(10)


# # --- O(1)----

# def add_item(n):
#     return n + n

# print(add_item(5))


# # ---- O(log n) ---
# data =[1, 2, 3, 4, 5, 6, 7, 8]

