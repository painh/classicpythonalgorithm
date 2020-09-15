from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V')  # 변수 타입
D = TypeVar('D')  # 도멩니 타입


class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constrainsts: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constrainsts[variable] = []
            if variable not in self.domains:
                raise LookupError("모든 변수에 도메인이 할당 되어야 합니다.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("제약 조건 벼수가 아닙니다.")
            else:
                self.constrainsts[variable].append(constraint)

    def consistent(self, variable: V, assigment: Dict[V, D]) -> bool:
        for constraint in self.constrainsts[variable]:
            if not constraint.satisfied(assigment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # asigment는 모든 변수가 할당될 떄 완료된다.(기저조건)
        if len(assignment) == len(self.variables):
            return assignment

        # 할당되지 않은 모든 변수를 가져온다
        unassigned: List[V] = [
            v for v in self.variables if v not in assignment]

        # 할당되지 않은 첫번쨰 변수의 가능한 모든 도메인값을 가져온다
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # local_assignment 값이 알관적이면 재귀 호출한다
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(
                    local_assignment)
                # 결과를 찾디 못하면 백트래킹을 종료한다. -> 반대 아님?
                if result is not None:
                    return result
        return None
