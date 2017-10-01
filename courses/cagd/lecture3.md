### Date : 22 sept
These notes might be wrong.

Properties of NURBS

1. $R^P_I(U)$ are rational functions of degree p

2. Non-negative if the weights are Non-negative

3. Local support : $R^p_i(u)$ is active on $[u_i,u_{i+p+1}]$

4. On $[u_i,u_{i+p+1}]$ there are at most p+1 active basis functions $R^p-{i-p}(u),....,R^p-{i}(u)$
5. Partition of unity
6. $m = n+p+1$
7. $R^p_i(u)$ is a composite curve of rational functions on $[u_i, u_{i+p+1})$.
8. At a knot of mult. k , $R^p_i(u)$ is $C^{p-k}$
9. If $w_i = c_i$ NURBS=B-spline
10. A clamped Nurbs curve though $b_0$ and $b_n$
11. Strong convex hull property (same as b-splines)
    $u \in [u_i,u_{i+1}) \rightarrow u$ is in the convex hull of $b_{i-p},...,b_i$ (this property holds for non-negative weights)
12. Local modification scheme. When you change the position of $B_i$ the curve only changes for $u \in [u_i,u_{i+p+1})$ (and you don't have to calculate all the new curves.)
13. Variation demonising property. (wiggle?)
14. Projective invariance

NURBS formula: $C(u)= \frac{1}{\sum N_i^p(u)w_i b_i}\sum N_i^p(u)w_i b_i$

Look at $b_k : u \in [u_k,u_{k+p+1})$

$C(u)= \frac{1}{\sum N_i^p(u)w_i b_i}\sum N_i^p(u)w_i b_i$

2-d NURBS $\leftrightarrow$ 3D B-spline
3d Nurmbs $\leftrightarrow$ 4d B-spline












BEZIER CURVES
Bezier curves are a form of parametric curve; they're a special case of cubic Hermite interpolation (as opposed to the linear interpolation of polygonal lines).
Hermite interpolation is a method of interpolating the points on the curve as a polynomial; in the context of the Bezier curve, this means that the curves are a sequence of cubic segments.

A Bezier Curve are generally defined using four control points. Two of these are the endpoints of the curve (knots), and the other two influence the shape/curvature of the curve. Since we did this for the fifth assignment, this is the one I guess we're most familiar with.

The main drawback of Bezier curves is that there is not much local control. Increasing the number of control points will not help as the number of control points is directly related to the degree of the curve.This is impractical considering that adding more control points does not necessarily increase local control. In fact, changing any control point inadvertently affects the entire curve because of the way the points are combined to make the curve.


B-SPLINE CURVES
B-spline curves can be considered a generalization of Bezier curves; in fact, they share many properties (they must obey the convex hull property, for one). However,  one of advantages in using B-splines is that they do provide affine invariance. This means that the coordinate system it is represented in can change without affecting the relative geometry of the curve; this is seen when the geometry of curve remains consistent when it is rotated, scaled, or translated.

B-spline curves also address the issue of local control. This means that that modifying one control point only affects the part of the curve near that control point, which is really useful when designing shapes.

It was mentioned in lecture that the B-Spline curve is so-called after the traditional spline used by draftsmen to manually draw curves. These splines were essentially long strips held down by lead weights, which allow the draftsmen to influence the shape of the curve. So I guess that's a good way to envision how a B-spline works; each control point is a lead weight that modifies one portion of the overall curve.


NURBS
Non-Uniform Rational B-Splines are a generalization of non-rational B-Splines, which in turn are generalizations of rational Bezier curves. When NURBS are referred to as rational, it means that they are invariant under perspective projection; this means that if you render two NURB objects that touch, they will still touch when rendered in perspective. The big difference between NURBS and B-Splines is that the control points are specified in homogenous coordinates. The former is also capable of a larger set of geometries.
