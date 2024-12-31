puzzleInput = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

# puzzleInput = '''66|44
# 14|81
# 14|63
# 95|17
# 95|47
# 95|81
# 31|66
# 31|78
# 31|79
# 31|87
# 32|57
# 32|66
# 32|42
# 32|19
# 32|47
# 13|64
# 13|95
# 13|19
# 13|31
# 13|81
# 13|37
# 52|87
# 52|84
# 52|37
# 52|36
# 52|67
# 52|66
# 52|81
# 21|67
# 21|72
# 21|76
# 21|36
# 21|25
# 21|82
# 21|77
# 21|68
# 34|95
# 34|93
# 34|31
# 34|74
# 34|84
# 34|32
# 34|52
# 34|36
# 34|49
# 48|49
# 48|29
# 48|44
# 48|54
# 48|34
# 48|38
# 48|76
# 48|89
# 48|85
# 48|14
# 75|93
# 75|57
# 75|68
# 75|59
# 75|19
# 75|66
# 75|13
# 75|63
# 75|74
# 75|31
# 75|73
# 59|98
# 59|17
# 59|47
# 59|64
# 59|52
# 59|29
# 59|89
# 59|42
# 59|72
# 59|44
# 59|79
# 59|94
# 57|87
# 57|91
# 57|37
# 57|81
# 57|48
# 57|54
# 57|47
# 57|64
# 57|21
# 57|42
# 57|93
# 57|94
# 57|66
# 87|66
# 87|79
# 87|84
# 87|37
# 87|73
# 87|64
# 87|22
# 87|94
# 87|48
# 87|42
# 87|19
# 87|82
# 87|89
# 87|17
# 73|79
# 73|92
# 73|82
# 73|52
# 73|49
# 73|29
# 73|44
# 73|47
# 73|22
# 73|64
# 73|67
# 73|72
# 73|98
# 73|54
# 73|17
# 89|98
# 89|38
# 89|36
# 89|49
# 89|34
# 89|92
# 89|25
# 89|72
# 89|75
# 89|68
# 89|74
# 89|14
# 89|44
# 89|95
# 89|13
# 89|52
# 42|67
# 42|17
# 42|14
# 42|79
# 42|21
# 42|29
# 42|54
# 42|89
# 42|38
# 42|75
# 42|72
# 42|22
# 42|64
# 42|46
# 42|76
# 42|49
# 42|92
# 22|68
# 22|44
# 22|82
# 22|54
# 22|67
# 22|76
# 22|36
# 22|13
# 22|77
# 22|34
# 22|29
# 22|92
# 22|31
# 22|21
# 22|74
# 22|49
# 22|14
# 22|72
# 82|57
# 82|13
# 82|32
# 82|34
# 82|98
# 82|74
# 82|29
# 82|49
# 82|76
# 82|46
# 82|44
# 82|89
# 82|31
# 82|92
# 82|77
# 82|72
# 82|14
# 82|36
# 82|52
# 67|36
# 67|19
# 67|63
# 67|31
# 67|81
# 67|57
# 67|77
# 67|87
# 67|78
# 67|13
# 67|95
# 67|37
# 67|76
# 67|84
# 67|75
# 67|59
# 67|66
# 67|32
# 67|68
# 67|25
# 77|95
# 77|32
# 77|13
# 77|87
# 77|57
# 77|91
# 77|31
# 77|19
# 77|93
# 77|42
# 77|64
# 77|47
# 77|84
# 77|25
# 77|78
# 77|63
# 77|73
# 77|81
# 77|59
# 77|66
# 77|74
# 92|66
# 92|95
# 92|81
# 92|84
# 92|13
# 92|78
# 92|76
# 92|75
# 92|19
# 92|77
# 92|87
# 92|36
# 92|59
# 92|63
# 92|93
# 92|94
# 92|31
# 92|74
# 92|57
# 92|68
# 92|37
# 92|32
# 79|67
# 79|98
# 79|49
# 79|82
# 79|68
# 79|34
# 79|75
# 79|29
# 79|14
# 79|89
# 79|44
# 79|74
# 79|22
# 79|52
# 79|92
# 79|46
# 79|21
# 79|54
# 79|85
# 79|72
# 79|13
# 79|38
# 79|77
# 84|21
# 84|82
# 84|94
# 84|48
# 84|59
# 84|98
# 84|29
# 84|47
# 84|81
# 84|17
# 84|89
# 84|44
# 84|91
# 84|37
# 84|64
# 84|42
# 84|85
# 84|19
# 84|22
# 84|73
# 84|66
# 84|54
# 84|63
# 84|79
# 64|89
# 64|17
# 64|67
# 64|21
# 64|44
# 64|68
# 64|46
# 64|82
# 64|75
# 64|49
# 64|76
# 64|48
# 64|54
# 64|14
# 64|85
# 64|22
# 64|98
# 64|29
# 64|38
# 64|34
# 64|72
# 64|79
# 64|92
# 64|52
# 19|91
# 19|94
# 19|73
# 19|89
# 19|29
# 19|48
# 19|44
# 19|64
# 19|66
# 19|37
# 19|98
# 19|82
# 19|21
# 19|59
# 19|17
# 19|47
# 19|49
# 19|72
# 19|54
# 19|79
# 19|22
# 19|85
# 19|34
# 19|42
# 98|29
# 98|74
# 98|46
# 98|14
# 98|34
# 98|36
# 98|67
# 98|44
# 98|49
# 98|75
# 98|38
# 98|77
# 98|32
# 98|78
# 98|52
# 98|31
# 98|57
# 98|72
# 98|92
# 98|76
# 98|95
# 98|68
# 98|25
# 98|13
# 94|21
# 94|85
# 94|38
# 94|79
# 94|73
# 94|47
# 94|29
# 94|72
# 94|54
# 94|34
# 94|17
# 94|48
# 94|46
# 94|44
# 94|49
# 94|64
# 94|42
# 94|89
# 94|52
# 94|91
# 94|22
# 94|82
# 94|67
# 94|98
# 47|42
# 47|98
# 47|64
# 47|46
# 47|48
# 47|17
# 47|34
# 47|52
# 47|89
# 47|29
# 47|67
# 47|92
# 47|54
# 47|44
# 47|38
# 47|79
# 47|22
# 47|72
# 47|75
# 47|49
# 47|14
# 47|85
# 47|21
# 47|82
# 54|74
# 54|52
# 54|82
# 54|34
# 54|68
# 54|31
# 54|77
# 54|21
# 54|49
# 54|29
# 54|75
# 54|46
# 54|44
# 54|72
# 54|38
# 54|76
# 54|13
# 54|98
# 54|36
# 54|89
# 54|25
# 54|67
# 54|14
# 54|92
# 91|79
# 91|22
# 91|82
# 91|89
# 91|54
# 91|21
# 91|47
# 91|44
# 91|67
# 91|73
# 91|34
# 91|92
# 91|98
# 91|49
# 91|72
# 91|29
# 91|85
# 91|38
# 91|52
# 91|48
# 91|64
# 91|17
# 91|42
# 91|46
# 46|19
# 46|75
# 46|36
# 46|31
# 46|57
# 46|13
# 46|25
# 46|84
# 46|81
# 46|67
# 46|52
# 46|32
# 46|14
# 46|68
# 46|78
# 46|93
# 46|74
# 46|76
# 46|92
# 46|77
# 46|95
# 46|87
# 46|63
# 46|66
# 76|68
# 76|36
# 76|25
# 76|57
# 76|87
# 76|31
# 76|73
# 76|19
# 76|91
# 76|66
# 76|81
# 76|84
# 76|37
# 76|32
# 76|63
# 76|78
# 76|95
# 76|13
# 76|74
# 76|77
# 76|59
# 76|47
# 76|94
# 76|93
# 68|84
# 68|91
# 68|73
# 68|63
# 68|95
# 68|31
# 68|19
# 68|59
# 68|66
# 68|25
# 68|36
# 68|42
# 68|94
# 68|93
# 68|13
# 68|57
# 68|37
# 68|32
# 68|87
# 68|47
# 68|78
# 68|74
# 68|81
# 68|77
# 72|31
# 72|36
# 72|84
# 72|87
# 72|63
# 72|93
# 72|76
# 72|46
# 72|25
# 72|14
# 72|77
# 72|32
# 72|49
# 72|95
# 72|78
# 72|13
# 72|57
# 72|38
# 72|67
# 72|68
# 72|74
# 72|92
# 72|52
# 72|75
# 85|21
# 85|92
# 85|72
# 85|46
# 85|54
# 85|44
# 85|74
# 85|13
# 85|98
# 85|14
# 85|76
# 85|31
# 85|77
# 85|22
# 85|68
# 85|89
# 85|34
# 85|29
# 85|38
# 85|75
# 85|52
# 85|67
# 85|82
# 85|49
# 25|59
# 25|48
# 25|78
# 25|93
# 25|95
# 25|63
# 25|32
# 25|94
# 25|73
# 25|81
# 25|85
# 25|66
# 25|37
# 25|22
# 25|19
# 25|42
# 25|79
# 25|64
# 25|84
# 25|17
# 25|91
# 25|47
# 25|87
# 25|57
# 37|46
# 37|44
# 37|34
# 37|82
# 37|59
# 37|79
# 37|48
# 37|94
# 37|64
# 37|73
# 37|91
# 37|47
# 37|98
# 37|38
# 37|42
# 37|49
# 37|89
# 37|17
# 37|22
# 37|85
# 37|29
# 37|21
# 37|72
# 37|54
# 36|95
# 36|85
# 36|19
# 36|78
# 36|32
# 36|37
# 36|63
# 36|57
# 36|25
# 36|91
# 36|87
# 36|66
# 36|64
# 36|17
# 36|94
# 36|42
# 36|48
# 36|84
# 36|93
# 36|73
# 36|79
# 36|59
# 36|47
# 36|81
# 78|66
# 78|19
# 78|42
# 78|82
# 78|21
# 78|79
# 78|81
# 78|37
# 78|84
# 78|89
# 78|94
# 78|17
# 78|63
# 78|91
# 78|87
# 78|93
# 78|54
# 78|48
# 78|85
# 78|22
# 78|73
# 78|64
# 78|59
# 78|47
# 74|81
# 74|84
# 74|87
# 74|19
# 74|36
# 74|42
# 74|13
# 74|59
# 74|32
# 74|64
# 74|66
# 74|91
# 74|78
# 74|94
# 74|63
# 74|25
# 74|95
# 74|47
# 74|37
# 74|57
# 74|93
# 74|17
# 74|73
# 74|31
# 63|81
# 63|64
# 63|22
# 63|94
# 63|37
# 63|73
# 63|47
# 63|44
# 63|82
# 63|89
# 63|66
# 63|54
# 63|98
# 63|21
# 63|59
# 63|29
# 63|79
# 63|19
# 63|91
# 63|17
# 63|85
# 63|42
# 63|34
# 63|48
# 93|94
# 93|54
# 93|81
# 93|84
# 93|98
# 93|17
# 93|64
# 93|85
# 93|37
# 93|91
# 93|89
# 93|66
# 93|82
# 93|63
# 93|47
# 93|42
# 93|22
# 93|48
# 93|79
# 93|19
# 93|73
# 93|59
# 93|21
# 93|44
# 81|64
# 81|48
# 81|21
# 81|79
# 81|89
# 81|44
# 81|17
# 81|98
# 81|72
# 81|34
# 81|22
# 81|59
# 81|94
# 81|37
# 81|42
# 81|91
# 81|54
# 81|73
# 81|29
# 81|19
# 81|85
# 81|66
# 81|47
# 81|82
# 17|34
# 17|38
# 17|85
# 17|46
# 17|22
# 17|79
# 17|89
# 17|29
# 17|98
# 17|14
# 17|82
# 17|75
# 17|49
# 17|76
# 17|44
# 17|68
# 17|77
# 17|67
# 17|54
# 17|48
# 17|92
# 17|72
# 17|21
# 17|52
# 38|63
# 38|31
# 38|32
# 38|92
# 38|95
# 38|81
# 38|84
# 38|68
# 38|87
# 38|67
# 38|46
# 38|19
# 38|52
# 38|13
# 38|93
# 38|75
# 38|76
# 38|74
# 38|25
# 38|36
# 38|77
# 38|78
# 38|57
# 38|14
# 29|49
# 29|68
# 29|25
# 29|77
# 29|57
# 29|52
# 29|92
# 29|95
# 29|76
# 29|14
# 29|38
# 29|75
# 29|74
# 29|72
# 29|13
# 29|32
# 29|93
# 29|31
# 29|36
# 29|78
# 29|46
# 29|67
# 29|34
# 29|87
# 49|31
# 49|74
# 49|57
# 49|63
# 49|93
# 49|75
# 49|68
# 49|38
# 49|67
# 49|46
# 49|52
# 49|36
# 49|77
# 49|81
# 49|84
# 49|76
# 49|25
# 49|14
# 49|32
# 49|92
# 49|78
# 49|95
# 49|13
# 49|87
# 44|72
# 44|67
# 44|75
# 44|52
# 44|25
# 44|32
# 44|14
# 44|57
# 44|78
# 44|34
# 44|76
# 44|95
# 44|77
# 44|92
# 44|74
# 44|87
# 44|36
# 44|29
# 44|49
# 44|38
# 44|13
# 44|31
# 44|46
# 44|68
# 66|79
# 66|94
# 66|98
# 66|21
# 66|48
# 66|37
# 66|49
# 66|85
# 66|38
# 66|91
# 66|73
# 66|89
# 66|29
# 66|59
# 66|64
# 66|82
# 66|54
# 66|17
# 66|42
# 66|72
# 66|34
# 66|47
# 66|22
# 14|74
# 14|32
# 14|57
# 14|93
# 14|59
# 14|76
# 14|19
# 14|36
# 14|77
# 14|68
# 14|95
# 14|25
# 14|91
# 14|66
# 14|87
# 14|94
# 14|78
# 14|75
# 14|13
# 14|37
# 14|31
# 14|84
# 95|19
# 95|87
# 95|91
# 95|82
# 95|94
# 95|78
# 95|42
# 95|93
# 95|54
# 95|37
# 95|21
# 95|59
# 95|84
# 95|66
# 95|85
# 95|64
# 95|79
# 95|63
# 95|73
# 95|48
# 95|22
# 31|32
# 31|64
# 31|91
# 31|73
# 31|59
# 31|63
# 31|81
# 31|37
# 31|93
# 31|57
# 31|94
# 31|36
# 31|95
# 31|84
# 31|19
# 31|48
# 31|25
# 31|47
# 31|17
# 31|42
# 32|78
# 32|93
# 32|94
# 32|48
# 32|84
# 32|91
# 32|37
# 32|17
# 32|73
# 32|54
# 32|85
# 32|95
# 32|64
# 32|22
# 32|63
# 32|59
# 32|81
# 32|79
# 32|87
# 13|63
# 13|94
# 13|47
# 13|32
# 13|48
# 13|25
# 13|66
# 13|78
# 13|36
# 13|42
# 13|57
# 13|17
# 13|93
# 13|91
# 13|87
# 13|84
# 13|73
# 13|59
# 52|75
# 52|19
# 52|14
# 52|13
# 52|76
# 52|95
# 52|68
# 52|74
# 52|25
# 52|32
# 52|57
# 52|63
# 52|93
# 52|92
# 52|78
# 52|77
# 52|31
# 21|52
# 21|34
# 21|44
# 21|74
# 21|14
# 21|29
# 21|46
# 21|75
# 21|89
# 21|32
# 21|49
# 21|92
# 21|13
# 21|31
# 21|38
# 21|98
# 34|75
# 34|92
# 34|76
# 34|67
# 34|14
# 34|68
# 34|46
# 34|77
# 34|38
# 34|13
# 34|87
# 34|25
# 34|78
# 34|57
# 34|72
# 48|82
# 48|72
# 48|68
# 48|79
# 48|75
# 48|77
# 48|74
# 48|22
# 48|67
# 48|21
# 48|46
# 48|92
# 48|98
# 48|52
# 75|84
# 75|95
# 75|78
# 75|87
# 75|81
# 75|32
# 75|77
# 75|37
# 75|76
# 75|91
# 75|25
# 75|36
# 75|94
# 59|48
# 59|91
# 59|54
# 59|46
# 59|22
# 59|49
# 59|73
# 59|21
# 59|34
# 59|38
# 59|85
# 59|82
# 57|17
# 57|78
# 57|95
# 57|85
# 57|84
# 57|79
# 57|19
# 57|22
# 57|63
# 57|73
# 57|59
# 87|59
# 87|63
# 87|21
# 87|91
# 87|98
# 87|47
# 87|93
# 87|81
# 87|54
# 87|85
# 73|42
# 73|38
# 73|89
# 73|85
# 73|21
# 73|14
# 73|34
# 73|46
# 73|48
# 89|57
# 89|67
# 89|31
# 89|46
# 89|29
# 89|77
# 89|32
# 89|76
# 42|48
# 42|52
# 42|98
# 42|34
# 42|82
# 42|44
# 42|85
# 22|38
# 22|75
# 22|52
# 22|98
# 22|89
# 22|46
# 82|25
# 82|75
# 82|68
# 82|67
# 82|38
# 67|93
# 67|74
# 67|92
# 67|14
# 77|36
# 77|37
# 77|94
# 92|25
# 92|14
# 79|76

# 93,36,64,57,94,66,13,32,37,78,73,19,25,84,17,31,87,47,42,59,81,91,95
# 31,14,72,52,46,38,49,76,74,22,98,68,29,75,89,21,77
# 21,25,67,34,75,29,52
# 34,72,85,91,42,29,82,98,19,79,44,47,89
# 42,17,79,85,54,21,89,98,34,72,38,92,75
# 74,13,31,36,25,63,37,59,64
# 95,92,75,77,46
# 36,78,84,81,66,59,91,47,64
# 54,82,29,49,38
# 73,42,64,17,48,79,85,82,98,29,72,49,52,67,92
# 32,79,37,84,59,64,22,66,57,78,93,85,42,95,17
# 82,89,98,44,29,34,49,38,52,92,76,13,32
# 95,78,93,84,81,19,94,73,47,64,17,48,21
# 36,25,32,78,87,93,84,63,81,66,59,94,91,47,42,64,17,48,79
# 44,29,49,46,92,76,77,74,13,25,32
# 48,85,22,89,44,29,34,46,52,92,14,75,77
# 44,54,19,73,22,59,91,82,48,17,79,85,42,66,47,94,21,98,89,81,29,64,63
# 36,57,87,93,63,19,66,59,94,91,73,47,42,64,17,48,79
# 74,36,78,13,95,67,49,31,25,92,32
# 64,92,73,72,22,79,44,21,89,52,49,48,85,54,38,98,82,47,17,29,34,42,46
# 36,34,31,74,77,49,52,68,76,72,46,82,92,98,67,21,89,54,29
# 46,92,14,75,76,77,13,31,25,32,57,95,87,63,19
# 77,74,31,36,25,32,57,95,93,63,81,66,37,59,94,91,42
# 47,85,22,54,21,89,44,29,52,67,14
# 48,22,54,21,89,98,44,72,46,52,67,92,76,68,77
# 37,42,64,22,29,34,38
# 19,17,93,81,87,21,85,48,37,91,59,47,66,94,22,54,42,64,84
# 68,29,34,98,75,79,72,82,85,44,52,77,48
# 72,38,52,14,77,74,57,93,84
# 29,72,49,46,52,14,13,36,57
# 54,85,34,72,67,76,17,75,82,21,46,49,14,89,44,22,68,79,52,38,29
# 81,19,37,59,94,91,73,47,48,85,22,54,21,89,44,29,34
# 77,13,87,49,29,46,25
# 84,94,37,95,75,68,66,59,25,76,74,19,31
# 22,82,29,14,77,74,31
# 19,42,57,95,94,63,84,47,78,85,93,79,17,73,87
# 76,21,44,31,75,68,34,29,52,67,82,46,38,72,74
# 75,14,57,74,95
# 72,87,76,46,14,38,84
# 94,95,85,84,32,87,17,47,22,19,93,48,59,63,57,79,78,91,37
# 34,64,49,72,44,89,17,21,79,66,94,37,47,22,85,98,29,54,59,91,48,82,73
# 37,63,36,13,93,14,25,68,76,31,81,87,78
# 44,82,46,89,67,92,22,73,17
# 68,31,57,78,66,91,47
# 44,29,34,52,92,68,74,13,36,25,32,57,78
# 54,34,72,44,31,13,21,22,75
# 25,57,93,19,37,17,85
# 54,82,42,59,93,21,79,22,19,78,91,17,66,85,47
# 77,31,36,25,32,57,95,78,87,63,81,66,37,59,91,47,42
# 52,94,17,82,29,85,79,49,47,64,73,91,72,22,48,21,34,38,89,54,42
# 76,77,98,72,34,92,95
# 14,63,49,32,68,57,78
# 89,98,29,38,46,52,67,31,36,32,57
# 98,29,34,72,49,38,52,92,14,76,68,74,13,25,95
# 48,22,66,84,73,21,54,89,93,85,59,91,82,98,79,42,19,94,17,63,37
# 87,54,89,85,66,47,91
# 66,59,94,91,42,22,89,44,29,72,49
# 63,81,19,37,59,94,91,73,47,42,64,79,85,22,21,98,29
# 82,38,29,54,44,89,75,67,42,85,52,48,64,21,92,72,46,98,49,17,34
# 57,94,81,87,37,42,36,84,19,63,48,95,17,64,32,66,73,91,93
# 82,44,72,49,38,75,76,68,13,36,32
# 67,92,75,76,68,74,13,31,32,57,95,78,87,93,63,81,19,66,37
# 92,14,75,76,74,13,36,25,32,57,95,78,87,93,84,63,81,19,66,37,59
# 72,59,42,37,38,48,64,34,21,29,17
# 25,46,31,95,87,76,75,32,74,67,29,36,13,49,72,14,52
# 36,81,63,77,74,57,42,95,87,78,94,73,19,91,31,59,84
# 78,87,81,73,42,64,48,79,82
# 17,48,79,85,22,54,82,89,98,44,34,72,49,67,75,76,68
# 46,52,67,92,14,75,76,68,77,74,13,31,36,32,57,95,78,87,93,84,63,81,19
# 93,84,63,81,19,66,37,59,94,91,73,47,42,64,17,48,79,22,54,21,82,89,98
# 21,34,29,89,67,48,75,79,85,98,54,64,76,14,44,82,22
# 94,81,42,22,21,84,66,85,98,59,44
# 66,63,93,77,57,84,78,31,13,74,81,14,76,25,19,95,37,32,75,36,59,87,92
# 94,47,64,17,48,79,85,21,82,89,98,29,34,72,49,46,52
# 52,67,92,14,75,77,31,32,57,63,66
# 38,67,31,68,46,44,29,98,74,92,72,34,36,49,75,77,32,52,82
# 92,14,75,68,77,13,25,32,78,87,93,84,19,66,59
# 22,37,54,21,42,63,78,91,93,19,66,87,47
# 31,36,25,32,57,95,93,19,73,47,48
# 91,94,17,79,21,73,29,72,59,34,46
# 75,98,92,76,25,46,89,44,31,13,14,29,38,21,34,74,82,72,68,77,67
# 95,78,87,81,66,37,94,47,42,17,48,79,21
# 59,72,42,85,73,29,79,17,49,54,82
# 59,42,48,79,85
# 81,13,77,78,31,68,74,59,25,84,92,76,66,14,19,57,37
# 76,81,78,36,59,73,13,87,57
# 34,49,38,46,52,67,92,14,75,76,68,77,74,13,31,36,25,32,57,95,78,87,93
# 89,92,38,98,13,52,76,77,57,74,75,36,32,25,72
# 81,37,94,42,48,79,85,22,54
# 25,32,57,78,93,84,81,19,66,37,59,94,91,73,47,42,64,17,48,79,85
# 48,79,85,22,54,21,82,89,98,44,29,34,72,49,38,46,52,67,92,14,75,68,77
# 98,47,17,29,54,82,89,19,91,73,66,48,94,79,64,72,21,34,59
# 31,13,54,98,74,49,36
# 54,21,82,72,42,47,91,89,49,66,94,64,17,85,22,48,59,98,29,73,79
# 94,98,59,42,91,48,17,82,37,38,72,49,54
# 81,19,37,47,79,85,89,44,34
# 84,37,91,63,59
# 46,67,92,68,77,31,36,25,57,87,93,84,63,81,19
# 73,63,85,82,91,81,44,66,94,98,79,54,89,42,19,47,29,17,21,48,59
# 76,81,68,74,93,19,37,32,94,13,14,87,36,78,95,25,75
# 72,49,38,46,67,92,14,75,76,68,77,74,13,31,36,25,32,57,95,78,87,93,84
# 66,37,59,94,17,21,44,29,49
# 32,19,87,47,81,37,73,57,48,64,36,91,63,31,84
# 14,34,95,76,87,57,36
# 52,67,92,14,75,76,68,77,74,13,31,36,32,57,95,78,87,93,84,63,81,19,66
# 59,54,85,64,84,63,66,91,93,37,47,95,17
# 44,29,34,72,49,38,67,92,14,76,68,77,74,31,36,25,32,57,78
# 72,67,46,52,95,87,74,76,75,13,25,38,34,78,77
# 82,91,64,29,47,48,37,63,79,85,19,81,89,44,98,17,54
# 36,72,34,32,75,77,92,25,52
# 42,47,91,81,57,37,32,94,77,19,66,36,84,13,93,95,59,78,25
# 19,66,94,73,47,82,89,34,72
# 66,48,37,57,42
# 74,31,25,57,95,78,87,93,63,66,37,59,94,91,73,47,64
# 92,76,77,31,36,57,84,63,59
# 29,49,14,68,77,13,31,57,87
# 19,37,67,63,66,81,25,32,31
# 98,44,29,34,72,38,52,67,92,14,75,68,77,74,13,25,32,57,95
# 17,85,22,21,89,44,72,38,46,52,92,14,68
# 42,82,22,67,72,29,14,47,52
# 57,73,59,81,36,77,25,95,63,78,84,37,31,66,74,47,91,93,32,42,94
# 85,54,89,44,34,46,75,74,13
# 13,36,25,32,19,73,17
# 36,25,32,57,95,78,87,93,63,81,19,66,37,59,94,91,73,47,42,64,17,48,79
# 22,54,89,44,29,72,49,46,52,67,92,76,77,74,31
# 93,84,59,73,47,42,64,85,82
# 13,31,36,32,78,87,93,19,37,94,91,47,42,64,17
# 79,85,22,54,21,82,89,98,44,29,34,72,49,38,46,52,67,92,14,75,76,68,77
# 54,44,72,22,68,48,52,29,77
# 38,52,67,14,76,77,74,25,32,57,95,87,81
# 63,98,89,21,84,44,91,19,94,22,17,82,79,64,42,54,47
# 14,49,54,67,72,85,82,29,68,21,98,38,52,44,79,34,74,76,77,46,92,22,89
# 59,19,29,72,79,89,44,37,21,17,73
# 19,66,94,91,42,79,85,22,54,89,98,29,34
# 73,47,64,17,79,85,21,89,98,44,29,34,72,49,38,46,52,67,92
# 72,38,14,32,57,95,84
# 44,21,14,77,49,98,25,74,72
# 34,47,46,48,82,14,52,72,29,38,54,44,49
# 89,98,29,49,38,67,14,68,31
# 17,42,22,85,73,38,79,92,47
# 25,87,19,66,37,91,42,64,17,79,85
# 52,67,92,76,77,74,13,25,32,95,78,87,84,19,66
# 93,63,94,47,42,64,48,85,22,82,98
# 13,31,36,25,57,95,78,87,93,84,63,81,66,37,59,91,73,42,17
# 78,84,63,81,19,66,37,59,91,73,47,64,17,48,79,54,82
# 81,19,66,92,77,76,75,67,93,57,74,84,14,87,95,13,25,68,32,36,52,63,31
# 74,13,31,36,25,32,57,78,87,84,63,81,19,37,59,94,91,73,47,42,64
# 75,93,78,92,34,95,87,49,13
# 42,64,17,48,85,22,54,21,82,89,98,44,29,34,67,92,75
# 91,98,21,47,89,94,22,81,79,73,63,29,66
# 68,77,13,31,36,25,32,57,95,87,93,84,63,81,19,66,37,94,91,73,47
# 47,64,17,48,44,38,46
# 93,68,75,67,63,92,14,37,77,74,81,13,57,95,76
# 87,66,19,63,84
# 19,94,76,66,78,93,63,68,74,37,14
# 42,47,59,32,37,78,57,31,63,87,84,48,91,66,81,25,64,19,95,17,93
# 68,76,13,14,78,95,52,72,25
# 36,67,82,52,29,68,21,89,49
# 75,76,68,77,74,13,31,36,25,78,87,93,84,63,81,59,91
# 82,89,98,44,29,34,72,38,46,52,67,92,14,75,76,68,77,74,13,31,36,25,32
# 76,68,74,31,36,25,32,57,87,84,63,81,59,91,73
# 77,95,81,25,31,78,32,46,93,63,19,87,52
# 57,95,78,87,93,84,63,19,66,59,91,73,42,64,48,79,54
# 95,78,87,81,19,66,47,42,64,17,79,85,22
# 72,34,73,54,98,79,17,47,49,94,44,89,42,85,48,91,82,22,29,64,59
# 44,78,38,76,46,14,57,29,72,31,49,77,25,52,92,13,95,36,67,68,32,75,34
# 91,48,22,89,47,64,82,73,21,34,85,44,42,54,59,38,72
# 57,31,87,75,13,67,32,77,37,66,93
# 67,92,14,76,77,74,13,31,36,25,32,57,95,78,87,93,63,81,19,66,37
# 66,77,31,74,37,84,59,95,68,19,87,73,36,63,57,78,93,47,32
# 52,76,68,36,32,95,87,81,66
# 48,52,82,89,67,34,72,44,73,17,64,21,22,85,79,49,91,98,46
# 85,59,22,46,89,72,29,44,47,17,42,48,64,38,94,34,54
# 36,25,57,95,78,87,93,84,63,81,19,37,59,94,91,73,47,42,64,17,79
# 31,32,57,95,87,84,63,59,94,73,47,42,64,17,48
# 59,44,22,85,47,42,81,17,66,94,21,91,48,29,19,54,82
# 13,14,72,25,75,21,34,38,52,74,76,92,68,89,46,36,77,29,67
# 64,17,79,22,54,89,98,44,34,72,38,46,52,67,92,75,76
# 49,42,85,29,98,94,79,47,38,54,22,46,89,34,21,44,64,82,59,48,72,73,91
# 79,21,98,29,34,49,38,46,52,67,92,14,76,68,77
# 38,46,67,92,14,76,68,74,31,36,25,32,57,95,78,93,84,63,81
# 91,47,42,64,17,79,85,22,54,21,89,98,29,34,72,49,38,46,67
# 81,76,59,87,84,66,32,78,95,63,74,25,75,14,94,19,31,36,77,57,68,93,37
# 54,22,59,37,95,57,17,19,64,42,84,66,91,93,81,78,47,79,87,94,48,63,73
# 87,59,64,54,21,82,89
# 72,49,46,52,67,92,75,76,25,57,95,93,84
# 46,75,74,25,32,57,63
# 89,94,21,98,17,54,22,91,44,49,79,82,48,66,34,47,72
# 63,36,73,47,25,19,68,59,37,94,87,91,66,32,57
# 52,66,87,19,68,95,13
# 13,81,77,75,68,76,92,37,84,67,63
# 98,38,68,92,74,77,29,34,85,75,82,72,44,46,21,13,89,67,22,52,14
# 49,89,14,76,29,68,75,92,32,98,74,82,72
# 84,36,57,37,94,25,76,68,32,59,81,87,75,77,95
# 57,95,93,84,19,37,94,91,48
# 95,78,13,93,68,81,31,36,77
# 78,66,25,36,64,37,91,73,32,84,48,42,79,81,57,47,95
# 85,22,54,72,38,52,67,14,13
# 17,79,82,98,44,29,68
# 46,44,42,17,98,94,54,72,48,22,79,73,29,47,91,59,21,82,34,64,49,85,89
# 91,73,47,64,17,48,79,22,21,98,29,34,72,38,46,52,67
# 75,76,74,36,32,57,78,93,84,63,81,66,37,59,94
# 89,85,17,48,67,82,72,49,29
# 75,74,87,93,19,94,91
# 13,32,87,93,81,91,73,42,17
# 37,64,85,54,82,72,38
# 68,31,57,95,87,63,81,66,47
# 77,81,87,38,63,13,74,67,14,31,46,32,36,92,93,68,76,57,52,78,75
# 57,95,78,87,93,84,63,81,19,66,37,59,94,91,73,47,42,64,48,79,85,22,54
# 63,81,66,37,59,94,91,73,47,64,48,79,85,22,54,21,82,89,98,44,29
# 38,34,32,68,36,13,89,31,76,72,74,92,29,75,57
# 64,82,89,34,44,38,54,98,47
# 25,74,31,75,78,37,68,32,84,36,59,87,92,19,93,81,63,57,77,76,66
# 37,93,95,87,19,79,17,42,85,32,22
# 13,67,75,76,31,57,14,38,72,49,98,44,29,34,25,46,74,32,77,89,68,36,52
# 81,47,79,63,54,42,87,17,37,59,66,64,93,85,82,73,91,19,84,21,48,94,22
# 49,38,46,52,67,92,75,76,68,74,13,31,36,25,32,57,95,78,87,84,63'''

import math
import re


lines = puzzleInput.split("\n")
rules = []
pages = []
correct_order = []
incorrect_order = []
total = 0


for line in lines:
    if re.match(r'\d+\|\d+', line):
        rules.append(line.strip())
    elif re.match(r'\d', line):
        pages.append(line.strip())


for printorder in pages:
    page_array = printorder.split(',')
    correct = True
    for i in range(len(page_array) - 1):
        if f"{page_array[i]}|{page_array[i+1]}" in rules:
            continue
        else:
            correct = False
            break
    if correct:
        correct_order.append(printorder)
    else:
    	incorrect_order.append(printorder)


for printorder in correct_order:
    page_array = printorder.split(',')
    mid = page_array[math.ceil(len(page_array) / 2) - 1]
    total += int(mid)

print("Part 1: ", total)
# print(correct_order)

for printorder in incorrect_order:
	page_array = printorder.split(',')
	
