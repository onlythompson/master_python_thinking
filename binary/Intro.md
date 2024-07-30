# Bit Masking: The Locker Room Access Card 🎭🔑

Let's continue with our gym locker room, but now imagine we're creating an access card system for different areas of the gym. This is where Bit Masking comes in handy!

## What is Bit Masking?

Bit Masking is like using a special access card that has specific holes punched in it. When you place this card over a set of switches, it only allows you to see or change certain switches while hiding others.

In our gym example:
- The access card is the "mask"
- The switches represent different areas of the gym
- Holes in the card allow access, while solid parts block access

## How Does It Work?

We use binary numbers to represent both the access card (mask) and the gym areas.

```python
class GymAccess:
    def __init__(self):
        self.areas = 0b11111111  # All areas open initially
        self.LOCKER_ROOM  = 0b00000001
        self.WEIGHT_ROOM  = 0b00000010
        self.CARDIO_AREA  = 0b00000100
        self.POOL         = 0b00001000
        self.SAUNA        = 0b00010000
        self.YOGA_STUDIO  = 0b00100000
        self.CAFE         = 0b01000000
        self.ADMIN_OFFICE = 0b10000000
```

## Basic Operations

1. **Check Access to an Area (Using AND &)**
   ```python
   def has_access(self, area):
       return bool(self.areas & area)
   ```
   This is like placing the access card over the switches and checking if a specific hole lines up.

2. **Grant Access to an Area (Using OR |)**
   ```python
   def grant_access(self, area):
       self.areas |= area
   ```
   This is like punching a new hole in the access card.

3. **Revoke Access to an Area (Using AND with NOT ~)**
   ```python
   def revoke_access(self, area):
       self.areas &= ~area
   ```
   This is like covering up a hole in the access card.

4. **Toggle Access to an Area (Using XOR ^)**
   ```python
   def toggle_access(self, area):
       self.areas ^= area
   ```
   This is like flipping a hole to a solid part or vice versa on the access card.

## Why Use Bit Masking?

1. **Efficient**: One number can represent access to multiple areas.
2. **Fast Operations**: Checking or changing access is very quick.
3. **Combinable**: You can easily create complex access patterns.

## Real-World Uses

- **Permissions Systems**: Managing user access rights in software
- **Graphics**: Applying filters or effects to specific parts of an image
- **Network Programming**: Managing network flags and options
- **Embedded Systems**: Controlling hardware registers efficiently

## Simple Example

```python
gym = GymAccess()

# Create a mask for a basic membership
basic_membership = gym.LOCKER_ROOM | gym.CARDIO_AREA | gym.CAFE

# Grant basic membership access
gym.areas &= basic_membership

print(gym.has_access(gym.LOCKER_ROOM))   # True
print(gym.has_access(gym.WEIGHT_ROOM))   # False
print(gym.has_access(gym.POOL))          # False

# Upgrade to include weight room access
gym.grant_access(gym.WEIGHT_ROOM)

print(gym.has_access(gym.WEIGHT_ROOM))   # True
```

In this scenario, we use bit masking to manage access to different areas of the gym efficiently. Each area is represented by a specific bit, and we can quickly check, grant, or revoke access using simple bitwise operations.

Remember, Bit Masking is all about using patterns of bits (the mask) to selectively interact with another set of bits, allowing for efficient and flexible management of multiple flags or options.