import argparse
import numpy as np
import librosa
import soundfile as sf
from typing import Tuple


class AudioAugmentor:
    def __init__(self, sample_rate: int):
        self.sample_rate = sample_rate



    def pitch_shift(self, signal: np.ndarray, n_steps: float = 0) -> np.ndarray:
        """Сдвиг тона (в полутоновом масштабе)"""
        if signal.ndim == 1:  # Моно
            return librosa.effects.pitch_shift(signal, sr=self.sample_rate, n_steps=n_steps)
        else:  # Стерео или многоканальный сигнал
            return np.array([librosa.effects.pitch_shift(signal[i], sr=self.sample_rate, n_steps=n_steps) for i in
                             range(signal.shape[0])])

    def add_noise(self, signal: np.ndarray, noise_factor: float = 0.005) -> np.ndarray:
        """Добавление случайного шума"""
        noise = np.random.randn(*signal.shape)
        augmented_signal = signal + noise_factor * noise
        return np.clip(augmented_signal, -1.0, 1.0)

    def change_volume(self, signal: np.ndarray, gain_db: float = 0.0) -> np.ndarray:
        """Изменение громкости"""
        gain = 10 ** (gain_db / 20)
        return signal * gain

    def augment(self, signal: np.ndarray) -> np.ndarray:
        """Основная функция аугментации"""
        augmented_signal = signal.copy()

        # # Применяем различные аугментации
        n_steps = np.random.uniform(-2, 2)
        augmented_signal = self.pitch_shift(augmented_signal, n_steps)

        noise_factor = np.random.uniform(0.001, 0.01)
        augmented_signal = self.add_noise(augmented_signal, noise_factor)

        gain_db = np.random.uniform(-6, 6)
        augmented_signal = self.change_volume(augmented_signal, gain_db)

        return augmented_signal


def load_audio_file(file_path: str) -> Tuple[np.ndarray, int]:
    """Загружает аудио файл и возвращает numpy массив и частоту дискретизации"""
    signal, sample_rate = librosa.load(file_path, sr=None, mono=False)
    return signal, sample_rate


def save_audio_file(file_path: str, signal: np.ndarray, sample_rate: int) -> None:
    """Сохраняет numpy массив в аудио файл"""
    sf.write(file_path, signal.T, sample_rate)


def main() -> None:
    parser = argparse.ArgumentParser(description="Audio augmentation tool")
    parser.add_argument("input_file", type=str, help="Path to the input audio file")
    parser.add_argument("output_file", type=str, help="Path to save the augmented audio file")
    args = parser.parse_args()

    # Загрузка аудио файла
    signal, sample_rate = load_audio_file(args.input_file)

    # Создание экземпляра аугментатора
    augmentor = AudioAugmentor(sample_rate)

    # Аугментация аудио сигнала
    augmented_signal = augmentor.augment(signal)

    # Сохранение аугментированного сигнала
    save_audio_file(args.output_file, augmented_signal, sample_rate)

    print(f"Файл сохранен по пути: {args.output_file}")


if __name__ == "__main__":
    main()
