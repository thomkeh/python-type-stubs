from typing import Optional, Tuple, overload, Sequence


class _VectorElementwiseProxy2:
    @overload
    def __add__(self, other: float) -> Vector2:
        ...

    @overload
    def __add__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __add__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __radd__(self, other: float) -> Vector2:
        ...

    @overload
    def __radd__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __radd__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __sub__(self, other: float) -> Vector2:
        ...

    @overload
    def __sub__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __sub__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __rsub__(self, other: float) -> Vector2:
        ...

    @overload
    def __rsub__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __rsub__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __mul__(self, other: float) -> Vector2:
        ...

    @overload
    def __mul__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __mul__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __rmul__(self, other: float) -> Vector2:
        ...

    @overload
    def __rmul__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __rmul__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __truediv__(self, other: float) -> Vector2:
        ...

    @overload
    def __truediv__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __truediv__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __rtruediv__(self, other: float) -> Vector2:
        ...

    @overload
    def __rtruediv__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __rtruediv__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __floordiv__(self, other: float) -> Vector2:
        ...

    @overload
    def __floordiv__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __floordiv__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __rfloordiv__(self, other: float) -> Vector2:
        ...

    @overload
    def __rfloordiv__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __rfloordiv__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __mod__(self, other: float) -> Vector2:
        ...

    @overload
    def __mod__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __mod__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __rmod__(self, other: float) -> Vector2:
        ...

    @overload
    def __rmod__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __rmod__(self, other: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __pow__(self, power: float) -> Vector2:
        ...

    @overload
    def __pow__(self, power: Vector2) -> Vector2:
        ...

    @overload
    def __pow__(self, power: _VectorElementwiseProxy2) -> Vector2:
        ...

    @overload
    def __rpow__(self, power: float) -> Vector2:
        ...

    @overload
    def __rpow__(self, power: Vector2) -> Vector2:
        ...

    @overload
    def __rpow__(self, power: _VectorElementwiseProxy2) -> Vector2:
        ...


class _VectorElementwiseProxy3:
    @overload
    def __add__(self, other: float) -> Vector3:
        ...

    @overload
    def __add__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __add__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __radd__(self, other: float) -> Vector3:
        ...

    @overload
    def __radd__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __radd__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __sub__(self, other: float) -> Vector3:
        ...

    @overload
    def __sub__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __sub__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __mul__(self, other: float) -> Vector3:
        ...

    @overload
    def __mul__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __mul__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __rmul__(self, other: float) -> Vector3:
        ...

    @overload
    def __rmul__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __rmul__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __truediv__(self, other: float) -> Vector3:
        ...

    @overload
    def __truediv__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __truediv__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __rtruediv__(self, other: float) -> Vector3:
        ...

    @overload
    def __rtruediv__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __rtruediv__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __floordiv__(self, other: float) -> Vector3:
        ...

    @overload
    def __floordiv__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __floordiv__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __rfloordiv__(self, other: float) -> Vector3:
        ...

    @overload
    def __rfloordiv__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __rfloordiv__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __mod__(self, other: float) -> Vector3:
        ...

    @overload
    def __mod__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __mod__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __rmod__(self, other: float) -> Vector3:
        ...

    @overload
    def __rmod__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __rmod__(self, other: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __pow__(self, power: float) -> Vector3:
        ...

    @overload
    def __pow__(self, power: Vector3) -> Vector3:
        ...

    @overload
    def __pow__(self, power: _VectorElementwiseProxy3) -> Vector3:
        ...

    @overload
    def __rpow__(self, power: float) -> Vector3:
        ...

    @overload
    def __rpow__(self, power: Vector3) -> Vector3:
        ...

    @overload
    def __rpow__(self, power: _VectorElementwiseProxy3) -> Vector3:
        ...


def enable_swizzling() -> None:
    ...


def disable_swizzling() -> None:
    ...


class Vector2:
    x: float
    y: float
    __hash__: None  # type: ignore

    @overload  # todo: these overload default values have incorrect initializers
    def __init__(self, x: Optional[float] = 0, y: Optional[float] = 0) -> None:
        ...

    @overload
    def __init__(self, x: Optional[Vector2] = 0, y: Optional[float] = 0) -> None:
        ...

    @overload
    def __init__(self, x: Optional[Tuple[float, float]] = 0, y: Optional[float] = 0) -> None:
        ...

    @overload
    def __init__(self, x: Optional[Sequence[float]] = 0, y: Optional[float] = 0) -> None:
        ...

    def __setitem__(self, key: int, value: float) -> None:
        ...

    @overload
    def __getitem__(self, i: int) -> float:
        ...

    @overload
    def __getitem__(self, s: slice) -> Sequence[float]:
        ...

    def __add__(self, other: Vector2) -> Vector2:
        ...

    def __sub__(self, other: Vector2) -> Vector2:
        ...

    @overload
    def __mul__(self, other: Vector2) -> float:
        ...

    @overload
    def __mul__(self, other: float) -> Vector2:
        ...

    def __rmul__(self, other: float) -> Vector2:
        ...

    def __truediv__(self, other: float) -> Vector2:
        ...

    def __floordiv__(self, other: float) -> Vector2:
        ...

    def dot(self, other: Vector2) -> float:
        ...

    def cross(self, other: Vector2) -> Vector2:
        ...

    def magnitude(self) -> float:
        ...

    def magnitude_squared(self) -> float:
        ...

    def length(self) -> float:
        ...

    def length_squared(self) -> float:
        ...

    def normalize(self) -> Vector2:
        ...

    def normalize_ip(self) -> None:
        ...

    def is_normalized(self) -> bool:
        ...

    def scale_to_length(self, value: float) -> None:
        ...

    def reflect(self, other: Vector2) -> Vector2:
        ...

    def reflect_ip(self, other: Vector2) -> None:
        ...

    @overload
    def distance_to(self, other: Vector2) -> float:
        ...

    @overload
    def distance_to(self, other: Sequence[float]) -> float:
        ...

    def distance_squared_to(self, other: Vector2) -> float:
        ...

    def lerp(self, other: Vector2, value: float) -> Vector2:
        ...

    def slerp(self, other: Vector2, value: float) -> Vector2:
        ...

    def elementwise(self) -> _VectorElementwiseProxy2:
        ...

    def rotate(self, angle: float) -> Vector2:
        ...

    def rotate_rad(self, angle: float) -> Vector2:
        ...

    def rotate_ip(self, angle: float) -> None:
        ...

    def rotate_ip_rad(self, angle: float) -> None:
        ...

    def angle_to(self, other: Vector2) -> float:
        ...

    def as_polar(self) -> Tuple[float, float]:
        ...

    @overload  # todo: these overload default values have incorrect initializers
    def from_polar(self, polar_value: Sequence[float]) -> None:
        ...

    @overload
    def from_polar(self, polar_value: Tuple[float, float]) -> None:
        ...

    @overload
    def update(self, x: Optional[float] = 0, y: Optional[float] = 0) -> None:
        ...

    @overload
    def update(self, x: Optional[Vector2] = 0, y: Optional[float] = 0) -> None:
        ...

    @overload
    def update(self, x: Optional[Tuple[float, float]] = 0, y: Optional[float] = 0) -> None:
        ...

    @overload
    def update(self, x: Optional[Sequence[float]] = 0, y: Optional[float] = 0) -> None:
        ...


class Vector3:
    x: float
    y: float
    z: float

    @overload  # todo: these overload default values have incorrect initializers
    def __init__(self, xyz: Optional[float] = 0) -> None:
        ...

    @overload
    def __init__(self, xyz: Optional[Tuple[float, float, float]] = 0) -> None:
        ...

    @overload
    def __init__(self, xyz: Optional[Sequence[float]] = 0) -> None:
        ...

    @overload
    def __init__(self, xyz: Optional[Vector3] = 0) -> None:
        ...

    @overload
    def __init__(self, x: int, y: int, z) -> None:
        ...

    def __setitem__(self, key: int, value: float) -> None:
        ...

    @overload
    def __getitem__(self, i: int) -> float:
        ...

    @overload
    def __getitem__(self, s: slice) -> Sequence[float]:
        ...

    def __add__(self, other: Vector3) -> Vector3:
        ...

    def __sub__(self, other: Vector3) -> Vector3:
        ...

    @overload
    def __mul__(self, other: Vector3) -> float:
        ...

    @overload
    def __mul__(self, other: float) -> Vector3:
        ...

    def __rmul__(self, other: float) -> Vector3:
        ...

    def __truediv__(self, other: float) -> Vector3:
        ...

    def __floordiv__(self, other: float) -> Vector3:
        ...

    def dot(self, other: Vector3) -> float:
        ...

    def cross(self, other: Vector3) -> Vector3:
        ...

    def magnitude(self) -> float:
        ...

    def magnitude_squared(self) -> float:
        ...

    def length(self) -> float:
        ...

    def length_squared(self) -> float:
        ...

    def normalize(self) -> Vector3:
        ...

    def normalize_ip(self) -> None:
        ...

    def is_normalized(self) -> bool:
        ...

    def scale_to_length(self, value: float) -> None:
        ...

    def reflect(self, other: Vector3) -> Vector3:
        ...

    def reflect_ip(self, other: Vector3) -> None:
        ...

    def distance_to(self, other: Vector3) -> float:
        ...

    def distance_squared_to(self, other: Vector3) -> float:
        ...

    def lerp(self, other: Vector3, value: float) -> Vector3:
        ...

    def slerp(self, other: Vector3, value: float) -> Vector3:
        ...

    def elementwise(self) -> _VectorElementwiseProxy3:
        ...

    def rotate(self, angle: float, axis: Vector3) -> Vector3:
        ...

    def rotate_rad(self, angle: float, axis: Vector3) -> Vector3:
        ...

    def rotate_ip(self, angle: float, axis: Vector3) -> None:
        ...

    def rotate_ip_rad(self, angle: float, axis: Vector3) -> None:
        ...

    def rotate_x(self, angle: float) -> Vector3:
        ...

    def rotate_x_rad(self, angle: float) -> Vector3:
        ...

    def rotate_x_ip(self, angle: float) -> None:
        ...

    def rotate_x_ip_rad(self, angle: float) -> None:
        ...

    def rotate_y(self, angle: float) -> Vector3:
        ...

    def rotate_y_rad(self, angle: float) -> Vector3:
        ...

    def rotate_y_ip(self, angle: float) -> None:
        ...

    def rotate_y_ip_rad(self, angle: float) -> None:
        ...

    def rotate_z(self, angle: float) -> Vector3:
        ...

    def rotate_z_rad(self, angle: float) -> Vector3:
        ...

    def rotate_z_ip(self, angle: float) -> None:
        ...

    def rotate_z_ip_rad(self, angle: float) -> None:
        ...

    def angle_to(self, other: Vector3) -> float:
        ...

    def as_spherical(self) -> Tuple[float, float, float]:
        ...

    def from_spherical(self, spherical: Tuple[float, float, float]) -> None:
        ...

    @overload
    def update(self, xyz: Optional[float] = 0) -> None:
        ...

    @overload
    def update(self, xyz: Optional[Tuple[float, float, float]] = 0) -> None:
        ...

    @overload
    def update(self, xyz: Optional[Sequence[float]] = 0) -> None:
        ...

    @overload
    def update(self, xyz: Optional[Vector3] = 0) -> None:
        ...

    def update(self, x: int, y: int, z: int) -> None:
        ...

