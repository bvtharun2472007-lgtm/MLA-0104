import math

# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of Sigmoid
def sigmoid_derivative(y):
    return y * (1 - y)


# ---------------- Input Values ----------------
x1 = 0.6
x2 = 0.4

# ---------------- Initial Weights ----------------
w13 = 0.5
w23 = 0.2
w14 = 0.7
w24 = 0.3
w35 = 0.6
w45 = 0.4

# ---------------- Target Output ----------------
target = 0.8

# ---------------- Learning Rate ----------------
lr = 0.5


# ---------- FORWARD PASS ----------

a3 = x1 * w13 + x2 * w23
y3 = sigmoid(a3)

a4 = x1 * w14 + x2 * w24
y4 = sigmoid(a4)

a5 = y3 * w35 + y4 * w45
y5 = sigmoid(a5)

print("Output Before Training =", round(y5, 4))


# ---------- BACKWARD PASS ----------

error = target - y5

delta5 = error * sigmoid_derivative(y5)

delta3 = sigmoid_derivative(y3) * (delta5 * w35)
delta4 = sigmoid_derivative(y4) * (delta5 * w45)

# Update Output Layer Weights
w35 = w35 + lr * delta5 * y3
w45 = w45 + lr * delta5 * y4

# Update Hidden Layer Weights
w13 = w13 + lr * delta3 * x1
w23 = w23 + lr * delta3 * x2
w14 = w14 + lr * delta4 * x1
w24 = w24 + lr * delta4 * x2


# ---------- FORWARD PASS AFTER TRAINING ----------

a3 = x1 * w13 + x2 * w23
y3 = sigmoid(a3)

a4 = x1 * w14 + x2 * w24
y4 = sigmoid(a4)

a5 = y3 * w35 + y4 * w45
y5 = sigmoid(a5)

print("Output After Training =", round(y5, 4))
