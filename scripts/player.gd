extends CharacterBody3D
# ─────────────────────────────────────────────────────────────────────────────
# player.gd
# Attached to the Player's CharacterBody3D root node.
# Handles gravity, jumping, and camera-relative WASD movement.
# ─────────────────────────────────────────────────────────────────────────────

# ── Movement constants ────────────────────────────────────────────────────────
const SPEED         : float = 6.0   # Horizontal top speed in metres per second
const JUMP_VELOCITY : float = 5.5   # Upward impulse applied when the player jumps
const GRAVITY       : float = 9.8   # Downward acceleration applied while airborne


func _physics_process(delta: float) -> void:

	# ── Gravity ───────────────────────────────────────────────────────────────
	# Accumulate downward velocity every frame the player is not touching ground.
	if not is_on_floor():
		velocity.y -= GRAVITY * delta

	# ── Jump ──────────────────────────────────────────────────────────────────
	# ui_accept maps to Space / Enter by default.
	# Only allow a jump when the character is standing on solid geometry.
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# ── Read raw directional input ────────────────────────────────────────────
	# get_vector returns a normalised 2-D stick value.
	# Axes: x = left(-1)..right(+1), y = up(-1)..down(+1)  (screen space)
	var raw_input := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")

	# ── Camera-relative direction ─────────────────────────────────────────────
	# We transform the flat input through the camera's horizontal orientation
	# so that "forward" always means "where the camera is looking."
	var camera   := get_viewport().get_camera_3d()
	var direction := Vector3.ZERO

	if camera:
		var cam_basis := camera.global_transform.basis

		# Camera looks down its local -Z axis; right is +X.
		var cam_forward := -cam_basis.z
		var cam_right   :=  cam_basis.x

		# Flatten onto the XZ plane so a pitched camera doesn't push us into
		# the ground or launch us into the air.
		cam_forward.y = 0.0
		cam_right.y   = 0.0
		cam_forward   = cam_forward.normalized()
		cam_right     = cam_right.normalized()

		# Combine the two axes with the raw input magnitudes.
		# raw_input.y is negative when "up / forward" is pressed, so negate it.
		direction = (cam_forward * -raw_input.y + cam_right * raw_input.x).normalized()

	# ── Apply horizontal velocity ─────────────────────────────────────────────
	if direction.length() > 0.0:
		velocity.x = direction.x * SPEED
		velocity.z = direction.z * SPEED

		# Rotate the character to face the direction of travel (instant snap).
		# Replace with slerp on rotation if you want gradual turning later.
		rotation.y = atan2(direction.x, direction.z)
	else:
		# Friction: bleed off horizontal speed when no input is held.
		# move_toward(current, target, step) never overshoots zero.
		velocity.x = move_toward(velocity.x, 0.0, SPEED)
		velocity.z = move_toward(velocity.z, 0.0, SPEED)

	# ── Integrate & collide ───────────────────────────────────────────────────
	# move_and_slide applies velocity, resolves collisions, and updates
	# is_on_floor() / is_on_wall() for use in the next frame.
	move_and_slide()
