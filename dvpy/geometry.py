import numpy as np
import numpy.linalg as la

def project_point_onto_line(point, line_origin, line_vector):
  point_n = point - line_origin
  line_n = line_vector - line_origin
  return line_origin + line_n / la.norm(line_n) * np.dot(line_n, point_n) / la.norm(line_n)

def distance_from_point_to_plane(point,
                                 plane_origin = np.array([0, 0]),
                                 plane_normal = np.array([1, 0])):
  point_n = point - plane_origin
  plane_n = plane_normal - plane_origin
  return np.dot(point_n, plane_n) / la.norm(plane_n)

def distance_from_points_to_plane(points,
                                  plane_origin = np.array([0, 0]),
                                  plane_normal = np.array([1, 0])):
  return [[distance_from_point_to_plane(p, plane_origin, plane_normal) for p in r]
                                                                           for r in points]

def generate_circle(cx = 0.0, cy = 0.0, r = 1.0, N = 6):
  angle = np.asarray([np.float64(i) for i in range(N)]) * 2.0 * np.pi / N
  real = r * np.cos(angle) + cx
  imag = r * np.sin(angle) + cy
  return np.array([real, imag]).transpose()
