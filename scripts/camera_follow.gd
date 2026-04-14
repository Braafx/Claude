extends Camera3D
# ─────────────────────────────────────────────────────────────────────────────
# camera_follow.gd
# Smooth third-person follow camera.
# Attach to a Camera3D node in the World scene and set `target` in the
# Inspector to point at the Player node.
# ─────────────────────────────────────────────────────────────────────────────

# ── Inspector-editable properties ────────────────────────────────────────────

## NodePath to the node this camera will track (set in the Inspector).
@export var target : NodePath

## World-space offset added to the target's position to derive the camera goal.
## Positive Z = behind the player (assuming default Godot orientation).
## Increase Y to raise the camera, increase Z to zoom out.
@export var follow_offset : Vector3 = Vector3(0.0, 3.5, 6.0)

## Lerp factor controlling how quickly the camera catches up each frame.
## Higher = snappier; lower = floatier. Typical range: 3 – 10.
@export var follow_speed : float = 6.0

# ── Internal state ────────────────────────────────────────────────────────────
# Cached reference resolved once in _ready so we avoid get_node every frame.
var _target_node : Node3D


func _ready() -> void:
	# Resolve the exported NodePath into a live Node3D reference.
	# If `target` is left empty the camera simply stays put.
	if target and not target.is_empty():
		_target_node = get_node(target) as Node3D


func _process(delta: float) -> void:
	# ── Guard ─────────────────────────────────────────────────────────────────
	# is_instance_valid handles the case where the target node is freed at
	# runtime without crashing here.
	if not is_instance_valid(_target_node):
		return

	# ── Desired position ──────────────────────────────────────────────────────
	# Add the world-space offset directly to the target's global position.
	# This gives a fixed "behind and above" view regardless of player rotation.
	# To make the camera orbit around the player, rotate the offset vector by
	# the player's Y rotation before adding it here.
	var desired_pos : Vector3 = _target_node.global_position + follow_offset

	# ── Smooth follow ─────────────────────────────────────────────────────────
	# lerp() blends from current position toward desired position each frame.
	# Multiplying by delta keeps the speed frame-rate independent.
	global_position = global_position.lerp(desired_pos, follow_speed * delta)

	# ── Look at target ────────────────────────────────────────────────────────
	# Rotate the camera so it always faces the player's pivot point.
	# Vector3.UP prevents the camera from rolling sideways.
	look_at(_target_node.global_position, Vector3.UP)
